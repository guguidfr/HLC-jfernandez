export PYTHONPATH="$PYTHONPATH:$(pwd)/src"
uvicorn main:app --host 0.0.0.0 --port 5000
