#!/usr/bin/env ruby

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <text>"
else
  # Join multiple occurrences of "School" in the argument
  result = ARGV.join(' ').scan(/School/).join

  # Print the result
  puts result
end
