import subprocess
import time

def handler(request):
    while True:
        try:
            # Replace with your C++ compilation or Python task
            result = subprocess.run(['python3', 'm.py'], capture_output=True)
            if result.returncode != 0:
                return {
                    'statusCode': 500,
                    'body': 'Application crashed. Restarting...'
                }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f"Error: {str(e)}"
            }
        time.sleep(500)
    return {
        'statusCode': 200,
        'body': 'Application is running'
    }
