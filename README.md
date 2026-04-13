# Real-Time Data Platform

Production-grade streaming data platform.

## Project Principles

- Kafka is the event backbone and source of truth
- FastAPI is strictly an ingestion & contract boundary
- Raw data is immutable
- Curated data is derived and idempotent
- Streaming pipelines are replayable
- Orchestration is separated from streaming
- Scope is frozen via CHECKLIST.md