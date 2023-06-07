
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

"""" def big(a):
    return a > 5

def bigger(a, b):
    return a > b

check_output_1(big, 2, True)
check_output_1(big, 6, True)

check_output_2(bigger, 1,2, False)"""

s = "A̱χ’ejχsdən qən niɬej’ χa n̓axʲʷa qən ɢʷiɡʲilaswə’ɬej’ lej’əxʲ  kʲʷəχ’i̓ χa ɢəjuɬwə’ɬej’. Om̓ənu’χʷ n̓in̓əxʲʷaɬa dɬəw̓ən wiwəqʷa ̓dɬəw̓ən t͡sit͡sat͡səj̓a dɬəw̓ənu’χʷ ɡʲiɡʲə’owɬnukʲʷ, ow’əm"
print(s.replace(" ", ""))