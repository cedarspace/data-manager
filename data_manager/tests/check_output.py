
def check_output_1(func, input_param1, expected_output):
    output = func(input_param1)
    if output == expected_output:
        print("PASSED: test for " + str(func) + " and " +
              str(input_param1) + " input and " +
              str(expected_output) + " expected output passed! " )

    else:
        print("FAILED: test didn't pass for " + str(func) + " and " +
              str(input_param1) + " input and " +
              str(expected_output) + " expected output "
                                     " ,the expected value is: "
              + str(output))



def check_output_2(func, input_param1, input_param2, expected_output):
    output = func(input_param1, input_param2)
    if output == expected_output:
        print("PASSED: test for " + str(func) + " and " +
              str(input_param1) + " and " + str(input_param2) +
              " input and " + str(expected_output) +
              " expected output passed!")
    else:
        print("FAILED: test didn't pass for " + str(func) + " and " +
              str(input_param1) + " and " + str(input_param2) +
              " input. Expected output: " + str(expected_output) +
              ", actual output: " + str(output))