# ==========================================
# STAGE 1: The Build & Compilation Layer
# ==========================================
FROM python:3.11-slim AS builder
WORKDIR /app

# Install system compilation tools needed for libraries like sentence-transformers
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Force pip to build dependencies ONLY using the lightweight CPU index wheel
RUN pip install --no-cache-dir --user -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# ==========================================
# STAGE 2: The Final Clean Runtime Layer
# ==========================================
FROM python:3.11-slim AS runner
WORKDIR /app

# Copy ONLY the successfully installed small Python packages from Stage 1
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Pre-download the Hugging Face model so it embeds permanently in this layer
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Copy your actual local app files
COPY . .

EXPOSE 5000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

