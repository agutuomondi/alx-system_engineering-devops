#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <text>"
else
  # Extract uppercase letters
  result = ARGV[0].scan(/[A-Z]/).join

  # Print the result
  puts result
end
