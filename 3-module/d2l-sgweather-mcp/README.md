# Singapore Weather MCP Server

A simple Model Context Protocol (MCP) server that provides Singapore's 24-hour weather forecast from [data.gov.sg](https://data.gov.sg) in natural language format.

## Features

- Fetches real-time 24-hour weather forecast for Singapore
- Returns data in natural language format optimized for LLM consumption
- Includes temperature, humidity, wind conditions, and detailed period forecasts
- No API key required (uses public data.gov.sg API)

## Quick Start (Testing)

To test the MCP server locally:

```bash
npm install
npm start
```

This opens the MCP Inspector, an interactive interface where you can:
- View available tools
- Invoke `get_singapore_weather`
- See formatted weather responses

**Note:** `npm start` is for testing only. MCP clients will start the server automatically when needed.

## Using as an MCP Server

MCP servers use **stdio transport** - they are started on-demand by MCP clients and communicate via standard input/output. You don't need to run the server in the background.

### Claude Desktop

Add to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "sgweather": {
      "command": "node",
      "args": ["/absolute/path/to/sgweather-mcp/server.js"]
    }
  }
}
```

Claude Desktop will automatically start the server when needed and communicate with it via stdio.

### Other MCP Clients

Any MCP client can connect by spawning the server as a subprocess:

```javascript
// Example: MCP client spawns the server
const server = {
  command: "node",
  args: ["/path/to/server.js"]
};
```

The server starts when the client connects and exits when the client disconnects.

## Available Tools

### `get_singapore_weather`

Retrieves the current 24-hour weather forecast for Singapore.

**Parameters**: None

**Returns**: Natural language formatted weather report including:
- Last updated timestamp
- Overall temperature range
- Humidity range
- Wind speed and direction
- Forecast summary
- Detailed forecasts by time periods (morning, afternoon, night)
- Regional variations if applicable

## Example Output

```
Singapore 24-Hour Weather Forecast
=====================================

Last Updated: 29/10/2025, 5:40:00 pm

Overall Conditions:
- Temperature: 25°C to 34°C
- Humidity: 50% to 85%
- Wind: SW at 10-25 km/h

Forecast Summary:
Partly cloudy skies expected throughout the day...

Detailed Forecast by Period:

29 Oct, 6:00 pm to 30 Oct, 6:00 am:
  Partly Cloudy (Night)
  All regions: Partly Cloudy (Night)

...

Data source: data.gov.sg
```

## Data Source

Weather data is sourced from Singapore's open government data portal:
- API Endpoint: `https://api-open.data.gov.sg/v2/real-time/api/twenty-four-hr-forecast`
- Provider: data.gov.sg
- Update Frequency: Real-time

## Requirements

- Node.js 16+ (ESM support)
- Internet connection to access data.gov.sg API

## Project Structure

```
sgweather-mcp/
├── server.js       # Main MCP server implementation
├── package.json    # Node.js dependencies
└── README.md       # This file
```

## Note

This is a demo project for educational purposes and is not intended for production use.
