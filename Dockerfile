FROM public.ecr.aws/lambda/python:3.13

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Upgrade pip first
RUN pip install --upgrade pip

# Install the packages
RUN pip install -r requirements.txt

# Copy all files in root
COPY ./ ${LAMBDA_TASK_ROOT}/

# Set the CMD to handler
CMD [ "main.lambda_handler" ]
