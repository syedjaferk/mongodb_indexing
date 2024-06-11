from ulid import ulid

for itr in range(10):
    print(ulid.ULID().generate())