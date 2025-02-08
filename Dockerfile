FROM python:3.10.11

# Set working directory
WORKDIR /product_store

# Copy application files
COPY ./app/ ./app/
COPY run.py .
COPY wait-for-it.sh /usr/local/bin/wait-for-it

# Add and set permissions for wait-for-it script
RUN chmod +x /usr/local/bin/wait-for-it

# Install application dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose application port
EXPOSE 5000

# Load environment variables
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT
ARG DB_NAME


ENV DATABASE_URL="mysql+pymysql://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME"

# Use CMD to run the application
CMD ["sh", "-c", "wait-for-it db:3306 -- python run.py"]

# To run with env var
# docker run -d -p 5000:5000 \
#   -e DATABASE_URL="mysql+pymysql://brad:brad_steve@db:3306/product_store" \
#   bradesteve/product-store-backend





