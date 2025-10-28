## CoT

```
Q: Estimate how many taxis are actively carrying passengers in New York City at 8:00 pm on Sunday.

A: New York City's population is about 8.5 million people. On a typical Sunday evening, let's assume that around 2% of the population might be using taxis, which is 170,000 people. If we estimate that each taxi can carry an average of 2 passengers, we would need about 85,000 taxis to accommodate these passengers. However, not all taxis will be in use at the same time, so let's assume that only about 20% of the taxis are actively carrying passengers at any given moment. Therefore, 20% of 85,000 taxis is approximately 17,000 taxis.

Q: Estimate how many taxis are actively carrying passengers in Singapore at 8:00 pm on a weekday. Provide a single numeric estimate. Think clearly step by step.

A:
```


## Step by step reasoning

```
You are doing a Fermi estimate for Singapore at 8:00 pm on a weekday.
Reason step by step:
	1.	List key assumptions (population, fraction using taxis at that time, average ride duration, taxi fleet utilization).
	2.	Translate assumptions into intermediate quantities (rides/hour, taxis needed concurrently).
	3.	Compute the estimate and show intermediate math.
	4.	Provide a range (low/likely/high) and a one-sentence justification for each bound."""
```


## 2.3 Output formatting

```
Extract information from this text and return as JSON:

"John Smith, 28 years old, works as a software engineer in San Francisco."

Return JSON with keys: name, age, job, city

Return strictly only JSON, without any markdown formatting or explanations.
```
