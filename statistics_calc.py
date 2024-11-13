import numpy as np

def calculate(list):
  arr= np.array(list).reshape(3,3)
  calculations = {
      "mean":{
          "axis1": arr.mean(axis=0).tolist(),
          "axis2": arr.mean(axis=1).tolist(),
          "flattened": arr.mean().tolist()
      },
      "variance":{
          "axis1": arr.var(axis=0).tolist(),
          "axis2": arr.var(axis=1).tolist(),
          "flattened": arr.var().tolist()
      },
      "standard deviation":{
          "axis1": arr.std(axis=0).tolist(),
          "axis2": arr.std(axis=1).tolist(),
          "flattened": arr.std().tolist()
      },
      "max":{
          "axis1": arr.max(axis=0).tolist(),
          "axis2": arr.max(axis=1).tolist(),
          "flattened": arr.max().tolist()
      },
      "min":{
          "axis1": arr.min(axis=0).tolist(),
          "axis2": arr.min(axis=1).tolist(),
          "flattened": arr.min().tolist()
      },
      "sum":{
            "axis1": arr.sum(axis=0).tolist(),
          "axis2": arr.sum(axis=1).tolist(),
          "flattened": arr.sum().tolist()}
  }
  return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))