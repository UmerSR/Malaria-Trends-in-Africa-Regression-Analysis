# Malaria-Trends-in-Africa-Regression-Analysis

## Part 1: Linear Regression Analysis

This project aims to perform a linear and polynomial regression analysis on the incidence of Malaria in Africe between 2000 and 2015 in order to identify the areas at highest potential risk, allowing for insight into what areas would most benefit from interventionist policies.

The below image is of a linear regression on the entire continent's incidence data by year, alongside a 95% confidence interval. The results display a clear downward trajectory in malaria incidence over time.

![image](https://user-images.githubusercontent.com/22961577/152194140-023d9e7a-9e93-482e-b816-6e3b1d8eb673.png)

However, further perusing the data reveals more worrying information. For example, considering Nigeria's incidence rates in isolation show a steady overall increase, even though this data is clearly not modelled using a linear regression model.

![Nigeria scatter](https://user-images.githubusercontent.com/22961577/152194669-683552bb-e490-4901-9eae-f1442634d12e.png)

Looking at South Africa's incidence rates, it can be seen that reported cases, although still not modelled well linearly, show a steady decrease over time. However, it remains the case that South Africa's incidence rate is about 3.75 times that of Nigeria's despite the opposing rates of change

![South Africa scatter](https://user-images.githubusercontent.com/22961577/152194697-f05fb83b-f537-4473-820a-9a7d5a3bd251.png)

## Part 2: Polynomial Regression Analysis

In order to account for the non-linear nature of the data seen in Nigeria, polynomial regression is employed instead of linear regression in pursuit of an effective model. This introduces a new hyperparameter in the form of the order of the polynomial. The caveat with this is that low-order polynomials are less sensitive to change, therefore may not model certain situations effectively, and higher-order polynomials may be too sensitive and cause the model to be overfitted on the data. This phenomenon is often known as the bias-variance tradeoff


![Nigeria poly](https://user-images.githubusercontent.com/22961577/152196021-87dffb9f-8ac6-4ec5-b1c8-9f9f4b0743a1.png)

As seen in the image above, using a quartec (polynomial of order 4) seems to model the data relatively well, and can be justifiably used to make predictions into the near future. Note that it isn't perfect, which is purposeful. If we make it go out of its way to fit the graph by increasing the order, it will be overfitted on the data and create unnatural regression curves, as shown below (using a 90-degree polynomial):

![Nigeria poly (1)](https://user-images.githubusercontent.com/22961577/152196451-4c705317-a87b-4372-9db2-20eb5792f344.png)

Evidently, this model does not hold much weight as predictions will account too much for the pecularities of the training data (the variance in the model is too high). Therefore the previous model with order 4 is more credible when conducting a predictive regression analysis.
