# 🌱 GreenScale AI

### Carbon-Aware Dynamic Multi-Cloud Workload Orchestrator

## What is GreenScale AI?

GreenScale AI is a project that tries to answer a simple question:

> **"If I have to run a workload, which cloud region is the better place to run it?"**

Normally, cloud scheduling focuses on things like **cost, speed, and available resources**. GreenScale AI adds another important factor — **carbon emissions**.

It looks at the current conditions of different cloud regions and recommends where a workload should run based on a balance between **carbon impact, cost, and performance**.

---

## The Problem

Cloud applications use a lot of computing power, which means they also consume a lot of energy.

The problem is that **not every cloud region has the same environmental impact**. One region might be running mainly on renewable energy, while another might have a much higher carbon intensity.

Traditional schedulers usually don't consider this when deciding where to run a workload.

**GreenScale AI aims to make this decision more environmentally aware without ignoring cost and performance.**

---

## How Does the Data Flow?

The basic idea is:

```text
                     User
                       │
                       │ Workload Request
                       ▼
                FastAPI Backend
                       │
              ┌────────┴────────┐
              ▼                 ▼
       Cloud Simulator    Workload Simulator
              │                 │
              │   Cloud Data    │ Workload Data
              └────────┬────────┘
                       ▼
                Optimization
                    Engine
                       │
                       ▼
              Best Cloud Region
                       │
                       ▼
                     User
```


## Project Phases

### Phase 1 — Backend & Basic Architecture

Set up the project structure and build the FastAPI backend.

### Phase 2 — Cloud Simulator

Create simulated cloud regions and generate data such as:

* CPU utilization
* Energy consumption
* Carbon intensity
* Cost
* Latency

### Phase 3 — Workload Simulator

Create different workloads with requirements like:

* CPU
* Memory
* Duration
* Priority
* Latency

### Phase 4 — Optimization Engine

Compare the available cloud regions and calculate which one is the better choice for a particular workload.

### Phase 5 — Carbon-Aware Scheduling

Use the optimization results to make dynamic workload placement decisions.

### Phase 6 — Evaluation & Visualization

Compare normal scheduling with carbon-aware scheduling and see how much we can improve:

* 🌱 Carbon emissions
* ⚡ Energy consumption
* 💰 Cost
* 🚀 Performance
* 📊 Resource utilization

---

## Goal

The goal of GreenScale AI is not simply to find the **cheapest** or **fastest** cloud region.

It is to find a **good balance between performance, cost, and environmental impact**.

> **Run workloads where the cloud is greener.**
