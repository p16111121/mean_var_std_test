import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    solve = np.array(list)
    solve = solve.reshape(3,3)
    print(solve)

    mean_row = [solve[0,:].mean(), solve[1,:].mean(), solve[2,:].mean()]
      
    mean_col= [solve[:,0].mean(), solve[:,1].mean(), solve[:,2].mean()]
    mean_all = solve.mean()
    var_row = [solve[0,:].var(), solve[1,:].var(),solve[2,:].var()]
    var_col = [solve[:,0].var(), solve[:,1].var(),solve[:,2].var()]
    var_all = solve.var()
    std_col =  [solve[:,0].std(), solve[:,1].std(), solve[:,2].std()]
    std_row =  [solve[0,:].std(), solve[1,:].std(), solve[2,:].std()]
    std_all = solve.std()
    max_col =  [solve[:,0].max(), solve[:,1].max(), solve[:,2].max()]
    max_row =  [solve[0,:].max(), solve[1,:].max(), solve[2,:].max()]
    max_all = solve.max()
    min_col =  [solve[:,0].min(), solve[:,1].min(), solve[:,2].min()]
    min_row =  [solve[0,:].min(), solve[1,:].min(), solve[2,:].min()]
    min_all = solve.min()
  

    return {'mean' : [mean_col,mean_row,mean_all],
          'variance': [var_col,var_row,var_all],
          'standard_deviation': [std_col,std_row,std_all],
          'max': [max_col,max_row,max_all],
          'min': [min_col,min_row,min_all]

         }
