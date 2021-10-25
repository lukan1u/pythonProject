def percentage(percent, whole):
	return (percent * whole) / 100.0

def evaporator(content, evap_per_day, threshold):
	days = 0
	thresholdPercentage = percentage(threshold, content)
	while thresholdPercentage <= content:
		content_used = percentage(evap_per_day, content)
		content = content - content_used
		days += 1
	return days

print(evaporator(10, 10, 5))