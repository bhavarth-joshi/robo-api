from robot.libraries.BuiltIn import BuiltIn

def parse_test_data(data):
  # Validate JSON structure
  if 'tests' not in data:
    raise ValueError('Invalid JSON format: Missing "tests" key')
  
  test_cases = []
  for test_case in data['tests']:
    if 'title' not in test_case or 'steps' not in test_case:
      raise ValueError('Invalid test case format')
    
    # Update to handle dictionary with "description" key
    steps = []
    for step in test_case['steps']:
      if 'description' not in step:
        raise ValueError('Invalid step format: Missing "description" key')
      steps.append(step['description'])
    
    test_cases.append({'title': test_case['title'], 'steps': steps})
  
  return test_cases


def create_robot_suite(test_cases):
  robot_suite = """
  Suite Test Cases
  """
  for test_case in test_cases:
    robot_suite += f"\n*** Test Case {test_case['title']}\n"
    for step in test_case['steps']:
      robot_suite += f"    {step}\n"
  
  return robot_suite

def execute_tests(test_cases):
  robot_suite = create_robot_suite(test_cases)
  # Use robot.api library to execute the suite
  results = BuiltIn().run_tests(robot_suite)
  # Process test results and return them
  return process_test_results(results)

def process_test_results(results):
  # Extract pass/fail information and other details
  # from the Robot Framework test results object
  processed_results = []
  for suite in results.suites:
    for test in suite.tests:
      processed_results.append({
        'test_case': test.name,
        'status': test.status,
        # Add other relevant details like logs or errors
      })
  return processed_results
