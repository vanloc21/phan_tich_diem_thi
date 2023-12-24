import subprocess

start = 4000001
end   = 4013134

file = open("a.txt", "w")

for sbd in range(start,end):
	command = 'curl -F "sobaodanh=0' + str(sbd) + '" https://diemthi.vnexpress.net/index/detail/sbd/0' + str(sbd) + '/year/2023'
	result = subprocess.check_output(command)

	file.write(str(result) + "\n")
