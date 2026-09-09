# 🧠 Recall

> Your thoughts, structured and searchable.

#### A full-stack personal knowledge management application featuring GPU-accelerated semantic search and Firestore vector search.


[![React](https://img.shields.io/badge/React-blue?logo=react&logoColor=white)](https://react.dev/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Zustand](https://img.shields.io/badge/State-Zustand-443E3E?logo=react&logoColor=white)](https://zustand.docs.pmnd.rs/)
[![Tiptap](https://img.shields.io/badge/Editor-Tiptap-black?logo=tiptap&logoColor=white)](https://tiptap.dev/)
[![Firebase](https://img.shields.io/badge/Firebase-Services-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com/)

[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/ML-PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![CUDA](https://img.shields.io/badge/GPU-CUDA-76B900?logo=nvidia&logoColor=white)](https://developer.nvidia.com/cuda)
[![Sentence Transformers](https://img.shields.io/badge/Embeddings-all--MiniLM--L6--v2-FFCC00?logo=huggingface&logoColor=black)](https://www.sbert.net/)

[![Firebase Auth](https://img.shields.io/badge/Auth-Firebase%20Authentication-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com/docs/auth)
[![Firestore](https://img.shields.io/badge/Database-Cloud%20Firestore-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com/docs/firestore)
[![Vector Search](https://img.shields.io/badge/Search-Firestore%20Vector%20Search-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com/docs/firestore/vector-search)

## 📺 Screenshots

| | | | |
| :----: | :---: | :---: | :---: |
| ![Home](assets/home.png) | ![Dashboard Dark Mobile](assets/dash%20dark%20mob.png) | ![Viewer Light](assets/viewer%20light%20mob.png) | ![Editor Dark](assets/editor%20dark%20mob.png) |

| | |
| :---: | :---: |
| ![Search Light](assets/search%20light.png) | ![Dashboard Dark](assets/dash%20dark.png) |
| ![Viewer Dark](assets/viewer%20dark.png) | ![Editor Light](assets/editor%20light.png) |

## 📋 Table of Contents
- [🔍 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏗️ Architecture Overview](#️-architecture-overview)
- [🔍 Semantic Search](#-semantic-search)
- [🧵 Sync Pipeline](#-sync-pipeline)
- [📊 Data Model](#-data-model)
- [🔒 Authentication & Security](#-authentication--security)
- [🚀 Performance](#-performance)
- [📋 Prerequisites](#-prerequisites)
- [⚙️ 1. Clone & Environment Setup](#️-1-clone--environment-setup)
- [🐳 2. Quick Start with Docker](#-2-quick-start-with-docker)
- [💻 3. Manual Local Development](#-3-manual-local-development)
- [📐 Architectural Design Decisions](#-architectural-design-decisions)
- [🔮 Future Improvements](#-future-improvements)
- [📄 License](#-license)

## 🔍 Overview

**Recall** is a full-stack personal knowledge base optimized for storing, organizing, and deeply exploring personal notes. 

Unlike traditional keyword-based matching, Recall translates the underlying context of your content using sentence embeddings and Firestore Vector Search to retrieve exact records based on their core **semantic meaning**.

## ✨ Key Features

### 🎨 Frontend Experience
* **Rich-Text Editor:** Interactive editing engine powered by TipTap.
* **Smart Folders:** Dynamic workflows for archiving, trashing, and restoring notes.
* **Flexible Taxonomy:** Pinning and custom categories for quick groupings.
* **Responsive Layout:** Fluid dark/light adaptive interfaces across mobile and desktop.

### 🧠 Semantic & Vector Search
* **Contextual Retrieval:** Pure semantic search driven by machine learning vector embeddings.
* **Isolated Sandbox:** Secure multi-user data isolation keeping user records distinct.
* **GPU Pipeline:** Asynchronous embedding generation utilizing multiple processing workers.
* **Traffic Throttling:** Smart backend embedding debounce and strict job deduplication.

## 🛠️ Tech Stack

### 🎨 Frontend
* **Core:** React
* **Language:** JavaScript
* **State Management:** Zustand
* **Text Engine:** TipTap
* **Services Integration:** Firebase SDK
* **Styling:** CSS

### 🐍 Backend
* **API Framework:** FastAPI
* **ASGI Server:** Uvicorn
* **Environment Variables:** python-dotenv
* **Firebase Admin:** firebase-admin
* **ML Inference Library:** SentenceTransformers
* **Deep Learning Runtime:** PyTorch
* **Hardware Compute Platform:** CUDA

### ☁️ Database & Infrastructure
* **Identity Protocol:** Firebase Authentication
* **NoSQL Catalog:** Cloud Firestore
* **Search Engine:** Firestore Vector Search

## 🏗️ Architecture Overview

The platform uses a decoupled, three-layer blueprint, consisting of a React frontend, Firebase infrastructure, and a Python AI backend.

<p align="center">
  <img alt="Recall System Architecture Dark" src="assets/architecture/dark.svg#gh-dark-mode-only" width="100%">
  <img alt="Recall System Architecture Light" src="assets/architecture/light.svg#gh-light-mode-only" width="100%">
</p>

### 📱 1. Frontend (React)
Manages localized state, event handling, and layout rendering.
* **Authentication:** Handles user sign-in and session state.
* **Note Management:** Standard CRUD operations, editing, and viewing.
* **Organization:** Category management for grouping notes.
* **Search Interface:** Triggers and displays semantic search requests.
* **UX/UI:** Fluid, responsive design with local UI state management.

### 🔥 2. Infrastructure & Auth (Firebase)
Serves as the secure global data catalog and security gate.
* **Authentication:** Manages secure user accounts.
* **Firestore Database:** Handles document persistence for notes.
* **Vector Search:** Performs scalable vector querying via Firestore.
* **Data Isolation:** Secures user-scoped notes and embedding data.

### 🐍 3. Backend API (Python)
Acts as the central Semantic Search & Embedding state synchronization worker.
* **Token Verification:** Unpacks and cryptographically checks incoming Firebase ID tokens.
* **Traffic Control:** Schedules incoming search requests to prevent pipeline choking.
* **AI Pipeline:** Generates query embeddings via machine learning model.
* **Vector Operations:** Executes vector searches and filters results.
* **Sync Engine:** Handles background synchronisation of note embeddings.

## 🔍 Semantic Search

Semantic search works by converting both notes and search queries into high-dimensional vector embeddings. This allows the system to match content based on conceptual meaning rather than exact keyword matches.

### 🔄 Search Pipeline

```text
        [ User Query ]
              │
              ▼
     [ React Frontend ]
              │  (Debounced)
              ▼
         [ FastAPI ]
              │
              ▼
[ Firebase ID Token Verification ]
              │
              ▼
  [ Thread-Safe Search Queue ]
              │
              ▼
       [ Search Worker ]
              │
              ▼
    [ Sentence Transformer ]
              │
              ▼
      [ Query Embedding ]
              │
              ▼
  [ Firestore Vector Search ]
              │
              ▼
        [ Filtering ]
              │
              ▼
      [ Matching Notes ]
              │
              ▼
      [ React Frontend ]
```

### 🛠️ Core Capabilities

* **User Isolation:** Restricts cross-user notes search with verified UID.
* **Taxonomy Filters:** Supports granular category filtering.
* **State Scoping:** Filters results across active, archived, or trashed states.
* **Distance Thresholds:** Employs Cosine-distance thresholding to ensure relevance.
* **Concurrency Guard:** Manages multiple concurrent users through a thread-safe request queue.

## 🧵 Sync Pipeline

Embedding generation is performed asynchronously so that note updates do not block the frontend application.

```text
       [ Firestore Change ]
                │
                ▼
      [ Firestore Listener ]
                │
                ▼
 [ 3-second Embedding Debounce ]
                │
                ▼
      [ Job Deduplication ]
                │
                ▼
   [ Min-Heap Priority Queue ]
                │
         ┌──────┴──────┐
         ▼             ▼
    [ Worker 1 ]  [ Worker 2 ]
         │             │
         └──────┬──────┘
                ▼
     [ Sentence Transformer ]
                │
                ▼
            [ CUDA ]
                │
                ▼
      [ Embedding Vector ]
                │
                ▼
   [ Firestore Vector Index ]
```

### ⏱️ Backend Debouncing & Deduplication

The note content in database needs to be updated much quicker than embeddings need to be calculated, to prevent data loss for user while also saving our computer resources. Thus, the backend engine implements a structural safety layer:

* **Cooldown Period:** The backend therefore applies an additional cooldown before processing an embedding job.
* **Job Deduplication:** If multiple updates arrive during this period, obsolete jobs are deduplicated.
* **Efficiency First:** This deduplication ensures that embedding computation is primarily performed for the latest version of the note.

## 📊 Data Model

### 📝 Notes
`notes/{noteId}`
```json
{
    "ownerId": "...",
    "collaborators": [],

    "title": "...",
    "content": { /*...TipTap JSON...*/ },
    "preview": "...",
    "categoryName": "...",
    "categoryId": "...",

    "pinned": false,
    "archived": false,
    "deleted": false,

    "created": serverTimestamp(),
    "updated": serverTimestamp(),
    "textLastUpdated": serverTimestamp(),
}
```

### 🧠 Note Embeddings
`noteEmbeddings/{noteId}`
```json
{
    "ownerId": "...",
    "categoryId": "...",
    "archived": false,
    "deleted": false,
    "embedding": Vector(), //384 dim
    "textLastUpdated": serverTimestamp(),
}
```

### 👤 Users
`users/{userId}`
```json
{
    "email": "example@mail.com",
    "displayName": "...",
    "categories": [
        {//Permanent
            "name": "General",
            "id": "x",
            "created": serverTimestamp(),
        },
        //User created ones
    ],
}
```

### 💡 Design Considerations

* **Separation of Concerns:** Embedding documents intentionally do not contain the complete note content because the frontend does not need embedding data when retrieving notes.
* **Shared Identifiers:** The note and corresponding embedding use the same document ID, eliminating the need for a redundant `noteId` field.

## 🔒 Authentication & Security

The frontend authenticates users using Firebase Authentication. Search requests send a Firebase ID token to the FastAPI backend.

```text
          [ React ]
              │
              ▼
 [ Query + Firebase ID Token ]
              │
              ▼
         [ FastAPI ]
              │
              ▼
       [ Verify Token ]
              │
              ▼
   [ Query + Trusted UID ]
              │
              ▼
       [ Search Queue ]
              │
              ▼
[ User-scoped Vector Search ]
```

### 🛡️ Multi-Tenant Isolation

* **Token-Derived Identity:** The backend does not trust a user-provided UID for tenant isolation.
* **Cryptographic Verification:** The UID used for search filtering is obtained strictly from the verified Firebase token.

## 🚀 Performance

Local embedding throughput bench-marked against text records:

* **Model Framework:** `all-MiniLM-L6-v2` via SentenceTransformers & PyTorch
* **Hardware Engine:** NVIDIA RTX 2050 (2048 CUDA Cores, Acceleration Enabled)
* **Average words/note:** 60

| Compute Configuration | Processing Throughput |
| :--- | ---: |
| Individual inference execution | ~150 notes/sec |
| Vector batch mode streaming | ~770 notes/sec |

> *Note: Metrics reflect local configurations and fluctuate based on text size and hardware constraints.*

## 📋 Prerequisites

Ensure you have Node.js (v18+), Python 3.11+, a Firebase Project, Docker Desktop, and optionally an NVIDIA GPU + CUDA for acceleration installed.

---

## ⚙️ 1. Clone & Environment Setup

### Step A: Clone the Repository
```bash
git clone https://github.com/FuzeIsHere/Recall.git
cd recall
```

### Step B: Configure Environment Variables
Create a `.env` file inside both the `client/` and `server/` directories by copying their respective `.env.example` files, then fill in your actual Firebase and API values.

### Step C: Add Firebase Service Account Key
Generate a new private key from your Firebase Console (Project Settings -> Service Accounts), rename it to `service-account-key.json`, and place it inside the `server/` directory.

---

## 🐳 2. Quick Start with Docker

Run the containerized services from the root directory:
```bash
docker compose up --build -d
```
Access the **Client** at `http://localhost:3000` and the **Server** at `http://localhost:5000`. Stop the application using `docker compose down`.

---

## 💻 3. Manual Local Development

### Frontend Setup
```bash
cd client
pnpm install
pnpm run dev
```

### Backend Setup
```bash
cd ../server
python -m venv venv
# Activate venv (venv\Scripts\activate on Windows or source venv/bin/activate on Linux/macOS)
pip install -r requirements.txt
python main.py
```

## 📐 Architectural Design Decisions

* **Why Firestore DB & Vector Index?**

  Firestore provides a unified persistence layer for notes and their
  corresponding embeddings, while its vector index enables semantic
  similarity search without requiring a separate vector database.

* **Why an Asynchronous Background Sync Pipeline?**

  Embedding generation is decoupled from the note CRUD and search
  request paths. A dedicated Firestore Listener Thread detects note
  changes and passes them through a 3-second embedding debounce and
  job-deduplication stage before they enter the processing queue.

* **Why a Min-Heap Priority Queue?**

  Pending embedding jobs are ordered by their next eligible execution
  time using a Min-Heap. Multiple embedding workers can then retrieve
  eligible jobs concurrently, generate their embeddings, and write the
  resulting vectors back to Firestore.

* **Why a Thread-Safe Search Queue?**

  Search requests from multiple users are coordinated through a
  thread-safe queue. After Firebase ID token verification, the trusted
  user UID is attached to the query before it enters the background
  search pipeline, ensuring that vector searches remain user-scoped.

* **Why `all-MiniLM-L6-v2` with CUDA?**

  `all-MiniLM-L6-v2` provides compact 384-dimensional dense vector representations
  suitable for semantic similarity search. CUDA acceleration allows
  embedding generation to be performed on the GPU, significantly
  increasing throughput when processing notes and search queries.


---

## 🔮 Future Improvements

- RAG-based question answering over notes
- Chunk-level embeddings for long notes
- Improved search ranking
- Additional note organization features
- Redis queue for notes embedding sync

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.