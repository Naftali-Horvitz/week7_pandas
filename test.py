

ip = input()

list_ip = ip.split('.')
list_ip = [int(x) for x in list_ip]
subnet = input()
subnet = int(subnet)
host_bit = 2 ** ( 8- (subnet % 8))
correct_byte = subnet // 8

network = list_ip[::]
network[correct_byte] = list_ip[correct_byte] // host_bit * host_bit
network[correct_byte + 1:] = [0 for _ in network[correct_byte + 1:]]

broadcast = network[::]
broadcast[correct_byte] += host_bit - 1 
broadcast[correct_byte + 1:] = [255 for _ in broadcast[correct_byte + 1:]]

next_subnet = broadcast[::]
next_subnet[correct_byte] += 1
next_subnet[correct_byte - 1] += next_subnet[correct_byte] // 255

next_subnet[correct_byte + 1 :] = [0 for _ in network[correct_byte + 1:]]




print(".".join(list_ip))
print(".".join(network))
print(".".join(broadcast))
print(".".join(next_subnet))


