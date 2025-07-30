# -- Vectors and Factors --

# Create items vector
items <- c('bag', 'watch', 'pen', 'bag', 'bag', 'watch', 'watch', 'pen', 'watch')
items # display items

# Factor
items_details <- summary(factor(items))
items_details # display items_details


# Assigning names to vector items
score <- c(88, 90, 71, 84)
names(score) <- c('STA111', 'STA234', 'STA123', 'STA212')

# Display score
score
