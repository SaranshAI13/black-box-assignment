# Investigation Summary

## My Approach

* Started by calling quote() with simple inputs to get a baseline. quote(2.0, 100, "standard") gave 330.0, which was my starting point.
* Varied one parameter at a time while keeping the rest fixed. This made it easy to see how weight, distance, and category each affect the price.
* Figured out the base formula first. By setting weight=1 and testing distance, I saw price increasing linearly at 2.5 per km with a 40 base for weight. So the formula is weight * 40 + distance * 2.5.
* Weight rounding took a little testing. Initially I thought math.ceil() was used on raw weight, but 0.1 kg and 0.5 kg gave same prices. Turns out weight rounds up to nearest 0.5 kg: ceil(w * 2) / 2.
* Category testing was simple. Tried all six categories. Electronics has 1.3x multiplier, fragile adds 150 flat. Books, clothing, food are same as standard.
* Express flag adds 80 flat fee to the shipping cost.
* Coupon WELCOME10 applies a 10% discount (0.9x).
* Minimum price cap is 100.0.
* Tested combination of express + coupon + fragile to verify order of operations.

## Hypotheses I Tested

* Thought weight was rounded to nearest whole integer. Wrong - it rounds to nearest 0.5 kg.
* Assumed WELCOME10 was a flat discount. Wrong - it is a 10% percentage discount.
* Thought category surcharge was calculated after express fee. Checked and verified step-by-step order.
* Tested if negative or invalid inputs break the code.
