# -*- mode: ruby -*-
# vi: set ft=ruby :
require 'vagrant-ansible'

Vagrant::Config.run do |config|
  config.vm.define :server do |server_config|
    server_config.vm.box = "precise64"
    server_config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    server_config.vm.host_name = "server"
    server_config.vm.forward_port 80, 8080
    server_config.vm.provision :shell, :inline => "sudo apt-get update"
    server_config.vm.provision :ansible do |ansible|
      ansible.playbook = "deploy.yml"
      ansible.hosts = "target"
      ansible.sudo = true
    end
  end
end
