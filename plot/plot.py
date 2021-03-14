import glob
import numpy as np
import matplotlib.pyplot as plt
import json
import sys
import math

in_file = sys.argv[1]
in_file = sys.argv[2]

with open(in_file, "r") as file:
    couch_data = json.loads(file.read())

with open(in_file, "r") as file:
    post_data = json.loads(file.read())

type_1_size = range(1000, 6000, 1000)
type_2_size = range(20000, 120000, 20000)
type_3_size = range(20000, 120000, 20000)
type_4_size = range(10000, 60000, 10000)



def format_couch(data, type, size_arr, nrounds):
    couch_data = \
        [
        sum
        (
            [
                float(data_point["time"][:-2])
                for data_point in data
                if data_point["type"] == type and data_point["size"] == size
            ]
        )
        /nrounds
        for size in size_arr
    ]

    return couch_data

def format_post(data, type, size_arr, nrounds):
    post_data = \
        [
        sum
        (
            [
                data_point["time"]
                for data_point in data
                if data_point["type"] == type and data_point["size"] == size
            ]
        )
        /nrounds
        for size in size_arr
    ]

    return post_data


def std_couch(mean, data, type, size_arr, nrounds):
    st = []
    mean_idx = 0
    for size in size_arr:
        p = 0
        for data_point in data:
            if(data_point["type"] == type and data_point["size"] == size) :
                # for i in range(nrounds):
                p += (float(data_point["time"][:-2]) - mean[mean_idx])**2
        print(p)
        d = math.sqrt(p/4)
        st.append(d)
        mean_idx += 1
        
    return st

def std_post(mean, data, type, size_arr, nrounds):
    st = []
    mean_idx = 0
    for size in size_arr:
        p = 0
        for data_point in data:
            if(data_point["type"] == type and data_point["size"] == size) :
                for i in range(nrounds):
                    p += (data_point["time"] - mean[mean_idx])**2
        print(p)
        d = math.sqrt(p/4)
        st.append(d)
        mean_idx += 1
        
    return st



# couch_type_1_mean = format_couch(couch_data, 1, type_1_size, 4)
# couch_type_2_mean = format_couch(couch_data, 2, type_2_size, 4)
# couch_type_3_mean = format_couch(couch_data, 3, type_3_size, 4)
# couch_type_4_mean = format_couch(couch_data, 4, type_4_size, 4)

# std_couch_1 = std_couch(couch_type_1_mean, couch_data,1, type_1_size,4 )
# std_couch_2 = std_couch(couch_type_2_mean, couch_data,2, type_2_size,4 )
# std_couch_3 = std_couch(couch_type_3_mean, couch_data,3, type_3_size,4 )
# std_couch_4 = std_couch(couch_type_4_mean, couch_data,4, type_4_size,4 )




# post_type_1_mean = format_post(post_data, 1, type_1_size, 4)
# post_type_2_mean = format_post(post_data, 2, type_2_size, 4)
# post_type_3_mean = format_post(post_data, 3, type_3_size, 4)
post_type_4_mean = format_post(post_data, 4, type_4_size, 4)


# print(couch_data[1]["time"])

# print(couch_type_2_mean)
# print(couch_type_3_mean)
# print(couch_type_4_mean)


# plt.errorbar(type_1_size, couch_type_1_mean, yerr=std_couch_1)
# plt.errorbar(type_2_size, couch_type_2_mean, yerr=std_couch_2)
# plt.errorbar(type_3_size, couch_type_3_mean, yerr=std_couch_3)
# plt.errorbar(type_4_size, couch_type_4_mean, yerr=std_couch_4)
plt.errorbar(type_4_size, post_type_4_mean, yerr=0)


plt.ylim([0, 20])


# if len(sys.argv) >= 4:
#     in_file1 = sys.argv[3]
#     with open(in_file1, "r") as file:
#         data1 = json.loads(file.read())
#     nrounds1 = int(sys.argv[4])
#     mean_tp1 = meanTp(data1, clients, nrounds1)
#     std_tp1 = stdTp(mean_tp1, data1, clients, nrounds1)
#     plt.errorbar(clients, mean_tp1, yerr=std_tp1)

# # plt.legend(["Throughput"])
# plt.xlabel("Number of clients")
# plt.ylabel("Throughput (requests per seccond)")


# print(mean_tp)
# plt.plot(
#     clients,
#     [
#         sum(
#             [
#                 datapoint["time"] / (datapoint["nclients"] * datapoint["nrequests"])
#                 for datapoint in data
#                 if datapoint["nclients"] == client
#             ]
#         )
#         / 5
#         for client in range(1, 11)
#     ],
# )


# plt.grid()
plt.show()
# plt.savefig(in_file + ".pdf")