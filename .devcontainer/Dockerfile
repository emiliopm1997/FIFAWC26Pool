FROM mcr.microsoft.com/devcontainers/base:ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# System dependencies + SQLite CLI
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    build-essential \
    make \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh \
    && bash miniconda.sh -b -p $CONDA_DIR \
    && rm miniconda.sh

ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda init bash

WORKDIR /workspace

COPY environment.yml /workspace/environment.yml

# Remove default channels at config level (prevents ToS issue)
RUN rm -f /opt/conda/.condarc

# Force conda-forge only
RUN conda config --system --remove-key channels || true
RUN conda config --system --add channels conda-forge
RUN conda config --system --set channel_priority strict

# Install mamba
RUN conda install -n base -c conda-forge mamba -y

# Create env (much more reliable)
RUN mamba env create -f environment.yml -vv

# Register Jupyter kernel
RUN conda run -n wc_pool_env python -m ipykernel install \
    --name wc_pool_env \
    --display-name "Python (wc_pool_env)"

# Activate env by default
ENV PATH=/opt/conda/envs/wc_pool_env/bin:$PATH

# Auto-activate environment in terminals
RUN echo "source /opt/conda/etc/profile.d/conda.sh" >> /root/.bashrc \
 && echo "conda activate wc_pool_env" >> /root/.bashrc

# Verify key packages
RUN python -c "import flask, sqlalchemy, pandas, jupyter"
