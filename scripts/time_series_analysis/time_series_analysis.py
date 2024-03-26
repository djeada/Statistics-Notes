import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

# Creating the dataset
data = {
    "Month": range(1, 13),
    "Sales": [100, 120, 110, 130, 140, 150, 160, 180, 170, 190, 200, 210]
}
df = pd.DataFrame(data)
df.set_index('Month', inplace=True)

# Fitting an optimized Simple Exponential Smoothing model
model_opt = SimpleExpSmoothing(df['Sales']).fit(optimized=True)

# Generating predictions using the optimized model
df['Optimized SES'] = model_opt.fittedvalues

# Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(df['Sales'], label='Actual Sales', color='blue')
plt.plot(df['Optimized SES'], label='Optimized SES', color='purple', linestyle='dashed')
plt.title('Sales Data and Optimized Simple Exponential Smoothing Predictions')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend()
plt.show()
