FROM python:3.13-slim

# System dependencies for the .NET runtime: libicu-dev (globalization)
# and libgdiplus + libfontconfig1 (System.Drawing / GDI+, required by
# image-processing and export paths on Linux)
# ttf-mscorefonts-installer (Microsoft core fonts) is in Debian's contrib
# component; its EULA is accepted non-interactively, and it downloads the
# fonts over HTTPS, hence ca-certificates.
RUN sed -i '/^Components:/s/main/main contrib/' /etc/apt/sources.list.d/debian.sources \
    && echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true \
        | debconf-set-selections \
    && apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev libfontconfig1 fontconfig libgdiplus ttf-mscorefonts-installer ca-certificates \
    && fc-cache -f \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
