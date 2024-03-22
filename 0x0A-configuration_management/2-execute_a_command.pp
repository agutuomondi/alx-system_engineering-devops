exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill -f "killmenow"',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep -f "killmenow"',
}

