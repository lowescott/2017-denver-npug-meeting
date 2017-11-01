# -*- mode: ruby -*-
# vi: set ft=ruby :

# Specify minimum Vagrant version and Vagrant API version
Vagrant.require_version '>= 1.6.0'

# Create and configure the VMs
Vagrant.configure('2') do |config|

  # Always use Vagrant's default insecure key
  config.ssh.insert_key = false

  # Set up the first vEOS switch
  config.vm.define 'veos01' do |veos01|

    # Specify the Vagrant box to use
    veos01.vm.box = 'arista-veos'

    # Forward ports as needed
    veos01.vm.network 'forwarded_port', guest: 22, host: 12201, id: 'ssh'
    veos01.vm.network 'forwarded_port', guest: 443, host: 14431, id: 'https'

    # Configure networks
    veos01.vm.network 'private_network', virtualbox__intnet: 'link_1', ip: '169.254.1.11', auto_config: false
    veos01.vm.network 'private_network', virtualbox__intnet: 'link_2', ip: '169.254.1.11', auto_config: false
    veos01.vm.network 'private_network', virtualbox__intnet: 'link_4', ip: '169.254.1.11', auto_config: false

    # Don't check for box updates
    veos01.vm.box_check_update = false

    # Set hostname
    veos01.vm.hostname = 'veos01'

    # Configure CPU and RAM
    config.vm.provider 'virtualbox' do |vb|
      vb.memory = '2048'
      vb.cpus = '1'
    end # srv.vm.provider
  end # config.vm.define 'veos01'

  # Set up the second vEOS switch
  config.vm.define 'veos02' do |veos02|

    # Specify the Vagrant box to use
    veos02.vm.box = 'arista-veos'

    # Forward ports as needed
    veos02.vm.network 'forwarded_port', guest: 22, host: 12202, id: 'ssh'
    veos02.vm.network 'forwarded_port', guest: 443, host: 14432, id: 'https'

    # Configure networks
    veos02.vm.network 'private_network', virtualbox__intnet: 'link_1', ip: '169.254.1.11', auto_config: false
    veos02.vm.network 'private_network', virtualbox__intnet: 'link_3', ip: '169.254.1.11', auto_config: false
    veos02.vm.network 'private_network', virtualbox__intnet: 'link_5', ip: '169.254.1.11', auto_config: false

    # Don't check for box updates
    veos02.vm.box_check_update = false

    # Set hostname
    veos02.vm.hostname = 'veos02'

    # Configure CPU and RAM
    config.vm.provider 'virtualbox' do |vb|
      vb.memory = '2048'
      vb.cpus = '1'
    end # srv.vm.provider
  end # config.vm.define 'veos02'
end # Vagrant.configure
