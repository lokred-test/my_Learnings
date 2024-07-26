# Python3 program to validate
# IP address using Regex
import re

# Function for Validating IP


def Validate_It(IP):

	# Regex expression for validating IPv4
	regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$"

	# Regex expression for validating IPv6
	regex1 = "((([0-9a-fA-F]){1,4})\\:){7}"\
			"([0-9a-fA-F]){1,4}"

	# p = re.compile(regex)
	p1 = re.compile(regex1)

	# Checking if it is a valid IPv4 addresses
	if (re.search(regex, IP)):
		return "Valid IPv4"

	# Checking if it is a valid IPv6 addresses
	elif (re.search(p1, IP)):
		return "Valid IPv6"

	# Return Invalid
	return "Invalid IP"

# Driver Code


# IP addresses to validate
IP = "255.120.223.13"
print(Validate_It(IP))

IP = "f:35:efa:23fe:2235:6565:aaab:0001"
print(Validate_It(IP))

IP = "2F33:12a0:3Ea0:0302"
print(Validate_It(IP))

# This code is contributed by avanitrachhadiya2155
