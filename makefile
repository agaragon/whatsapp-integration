# Makefile for AWS Lambda Deployment

# Variables
PYTHON_VERSION = 3.13
PLATFORM = manylinux2014_aarch64
PACKAGE_DIR = lambda_package
ZIP_FILE = lambda_function.zip
FUNCTION_NAME = handle_whatsapp_message

# Phony targets
.PHONY: all build deploy clean

# Default target
all: deploy

# Build the Lambda deployment package
build: $(PACKAGE_DIR) $(ZIP_FILE)

$(PACKAGE_DIR):
	@echo "Creating package directory..."
	mkdir -p $(PACKAGE_DIR)
	@echo "Copying application code and requirements..."
	cp app.py $(PACKAGE_DIR)/
	cp requirements.txt $(PACKAGE_DIR)/
	@echo "Installing dependencies for Lambda (Python $(PYTHON_VERSION), $(PLATFORM))..."
	python3 -m pip install --platform $(PLATFORM) --python-version $(PYTHON_VERSION) --implementation cp -r $(PACKAGE_DIR)/requirements.txt -t $(PACKAGE_DIR) --only-binary=:all: --no-cache-dir

$(ZIP_FILE): $(PACKAGE_DIR)
	@echo "Zipping deployment package..."
	cd $(PACKAGE_DIR) && zip -r ../$(ZIP_FILE) .
	@echo "Build complete: $(ZIP_FILE)"

# Deploy the Lambda function to AWS
deploy: build
	@echo "Deploying $(ZIP_FILE) to Lambda function $(FUNCTION_NAME)..."
	aws lambda update-function-code --function-name $(FUNCTION_NAME) --zip-file fileb://$(ZIP_FILE)
	@echo "Deployment complete."

# Clean up build artifacts
clean:
	@echo "Cleaning up build artifacts..."
	rm -rf $(PACKAGE_DIR)
	rm -f $(ZIP_FILE)
	@echo "Cleanup complete."


start-ngrok:
	ngrok http http://localhost:5000

start-flask:
	python app.py

# Create a temporary directory for building the package
create-lambda-package:
	mkdir -p lambda_package
	pip install -r requirements.txt -t lambda_package/
	cp app.py lambda_package/
	cd lambda_package && zip -r ../lambda_deployment.zip .
	rm -rf lambda_package

docker-lambda-package:
	mkdir -p lambda_build
	cp app.py requirements.txt lambda_build/
	docker run --rm --entrypoint /bin/sh -v "$$(pwd)/lambda_build":/var/task public.ecr.aws/lambda/python:3.11 \
		-c "pip install -r requirements.txt -t ."
	cd lambda_build && zip -r ../lambda_deployment.zip .
	rm -rf lambda_build



