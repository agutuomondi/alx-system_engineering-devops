#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <text>"
else
  # Match a string with exactly 10 digits
  result = ARGV[0].match(/^\d{10}$/)

  # Print the result or an appropriate message
  puts result ? result[0] : "No match found"
end
