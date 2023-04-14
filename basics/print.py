# full_name = "John Smith"
# # first_name
# # last_name
# #initials

# first_name = full_name.split(" ")[0]
# last_name = full_name.split(" ")[1]
# intials = first_name[0] + last_name[0]
# # print(first_name +" "+ last_name +" "+ intials)
# full_name.zfill(2)
# print(full_name.zfill(15)+" "+intials)

# print(list(range(10, 20)))

# from sys import argv
# def square(a):
#     return a * a

# print(f"Square of number {argv[1]} is {square(int(argv[1]))}")

nums = [100, 20, 30]

sum = 0
for num in nums:
    sum += num

nums.sort()
print(nums)
print(max(nums))
print(min(nums))