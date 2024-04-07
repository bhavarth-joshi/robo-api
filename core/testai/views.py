from django.shortcuts import render
from django.http import JsonResponse
from .utils import parse_test_data, execute_tests

def execute_tests_api(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      test_cases = parse_test_data(data)
      results = execute_tests(test_cases)
      return JsonResponse(results, safe=False)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=400)
  else:
    return JsonResponse({'error': 'Method not allowed'}, status=405)
