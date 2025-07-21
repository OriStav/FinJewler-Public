#%%

def calculate_annual_growth_rate(start_value, end_value, years):
  """
  annual_growth_rate = (growth_factor)^(1/years) - 1
  for israel's real estate Annual Growth Rate: 4.31%


  Calculates the annual growth rate of an asset.

  Args:
    start_value: The initial value of the asset.
    end_value: The final value of the asset.
    years: The number of years between the start and end values.

  Returns:
    The annual growth rate as a decimal.
  """

  growth_factor = end_value / start_value
  annual_growth_rate = growth_factor** (1 / years) - 1
  return annual_growth_rate

def real_estate_growth(by):
    #"https://www.mako.co.il/news-money/real_estate/Article-1e1141aae341a71027.htm"
    if by == "growth":
        import numpy as np
        annual_growth_rate  = np.mean([14,1,9,8,4,7,4,0,1,3,5])
        print(f"Annual Growth Rate: {annual_growth_rate:.2%}")
        
    else:
        # Example usage:
        start_value = 680
        end_value = 1580
        years = 2020 - 2000

        annual_growth_rate = calculate_annual_growth_rate(start_value, end_value, years)
        print(f"Annual Growth Rate: {annual_growth_rate:.2%}")

# real_estate_growth()