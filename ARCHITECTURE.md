# Architecture

# Architecture Overview

This platform is a real-time, event-driven data system designed for
scalable ingestion, schema evolution, replayability, and analytics.

## High-Level Flow

Client → FastAPI → Kafka → Snowflake Streaming → Raw Tables
                                      ↓
                                 Airflow (ELT, DQ, Backfill)
                                      ↓
                                 Curated Tables

## Component Roles

### FastAPI
- Authentication and authorization
- Schema validation with Pydantic
- Event versioning
- Event emission to Kafka
- Stateless, async ingestion

### Kafka
- Durable event log
- Ordering and replayability
- Consumer decoupling
- Backpressure handling

### Snowflake
- Raw: immutable event storage
- Curated: typed, deduplicated analytics tables

### Airflow
- Table creation
- Transformations
- Data quality checks
- Backfills and recovery workflows
