# IPsec Commands Reference

## Start/Stop StrongSwan
ipsec start       # Start StrongSwan daemon
ipsec stop        # Stop StrongSwan daemon
ipsec restart     # Restart StrongSwan

## Check Status
ipsec status      # Show active connections
ipsec statusall   # Show detailed status

## Check Version
ipsec version     # Show StrongSwan version

## Reload Config
ipsec reload      # Reload configuration files
ipsec rereadall   # Re-read all config files

## Debug/Logs
ipsec up hybrid-cloud      # Manually start tunnel
ipsec down hybrid-cloud    # Manually stop tunnel

## Show Encrypted Packets
ip xfrm state     # Show IPsec security associations
ip xfrm policy    # Show IPsec policies