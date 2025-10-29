#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fetch from "node-fetch";

const WEATHER_API_URL = "https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast";

async function fetchWeather() {
  try {
    const response = await fetch(WEATHER_API_URL);
    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    throw new Error(`Failed to fetch weather data: ${error.message}`);
  }
}

function formatWeatherToNaturalLanguage(data) {
  if (data.code !== 0) {
    return `Error: ${data.message || 'Unknown error from weather API'}`;
  }

  const { data: weatherData } = data;
  if (!weatherData) {
    return "No weather data available.";
  }

  const { records } = weatherData;
  if (!records || records.length === 0) {
    return "No weather records available.";
  }

  const record = records[0];
  const { general, timestamp, periods } = record;
  const { temperature, relativeHumidity, wind, forecast } = general;

  let output = "Singapore 24-Hour Weather Forecast\n";
  output += "=====================================\n\n";

  output += `Last Updated: ${new Date(timestamp).toLocaleString('en-SG', { timeZone: 'Asia/Singapore' })}\n\n`;

  output += "Overall Conditions:\n";
  output += `- Temperature: ${temperature.low}°C to ${temperature.high}°C\n`;
  output += `- Humidity: ${relativeHumidity.low}% to ${relativeHumidity.high}%\n`;
  output += `- Wind: ${wind.direction} at ${wind.speed.low}-${wind.speed.high} km/h\n\n`;

  if (forecast && forecast.text) {
    output += "Forecast Summary:\n";
    output += `${forecast.text}\n\n`;
  }

  if (periods && periods.length > 0) {
    output += "Detailed Forecast by Period:\n";
    periods.forEach((period) => {
      const startTime = new Date(period.timePeriod.start).toLocaleString('en-SG', {
        timeZone: 'Asia/Singapore',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: '2-digit'
      });
      const endTime = new Date(period.timePeriod.end).toLocaleString('en-SG', {
        timeZone: 'Asia/Singapore',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: '2-digit'
      });

      output += `\n${startTime} to ${endTime}:\n`;

      if (period.regions) {
        const uniqueForecasts = [...new Set(Object.values(period.regions).map(r => r.text))];
        if (uniqueForecasts.length === 1) {
          output += `  All regions: ${uniqueForecasts[0]}\n`;
        } else {
          output += "  Regional variations:\n";
          Object.entries(period.regions).forEach(([region, forecast]) => {
            output += `    ${region}: ${forecast.text}\n`;
          });
        }
      }
    });
  }

  output += "\n\nData source: data.gov.sg";

  return output;
}

const server = new Server(
  {
    name: "sgweather-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_singapore_weather",
        description: "Get the 24-hour weather forecast for Singapore from data.gov.sg. Returns temperature, humidity, wind conditions, and forecast periods in natural language format.",
        inputSchema: {
          type: "object",
          properties: {},
          required: [],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name } = request.params;

  if (name === "get_singapore_weather") {
    try {
      const weatherData = await fetchWeather();
      const formattedWeather = formatWeatherToNaturalLanguage(weatherData);

      return {
        content: [
          {
            type: "text",
            text: formattedWeather,
          },
        ],
      };
    } catch (error) {
      return {
        content: [
          {
            type: "text",
            text: `Error fetching weather data: ${error.message}`,
          },
        ],
        isError: true,
      };
    }
  } else {
    throw new Error(`Unknown tool: ${name}`);
  }
});

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Singapore Weather MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error:", error);
  process.exit(1);
});
