# Use Python 3.13 Bullseye
FROM python:3.13-bullseye

# Prevent Python from writing .pyc files and enable buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Set username and group for non-root user
ARG USERNAME=ulynks
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install system dependencies, create virtual environment, and update PATH globally
RUN set -eux; \
    # Create non-root user
    groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # Update system packages and install required dependencies
    && apt-get update \
    && apt-get upgrade -y \
    # Clean up APT cache
    && rm -rf /var/lib/apt/lists/* \
    # Install uv for Python package management
    && pip install uv \
    # Create virtual environment outside /work
    && uv venv /venv

# **Set PATH globally** so the virtual environment is always used
ENV PATH="/venv/bin:$PATH"

# Set work directory (but keep virtual environment outside of it)
WORKDIR /work

# Copy requirements files
COPY ./requirements.in ./

# Merge requirements and install dependencies in the virtual environment
RUN uv pip compile requirements.in -o requirements.txt \
    && uv pip sync requirements.txt

# Change ownership of /venv and /work to non-root user
RUN chown -R $USERNAME:$USERNAME /venv /work

# Switch to non-root user
USER $USERNAME
ENV PATH="/venv/bin:$PATH"
