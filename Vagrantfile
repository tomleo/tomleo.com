# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    host = RbConfig::CONFIG['host_os']

    config.vm.box = "ubuntu/trusty64"
    config.vm.box_check_update = false

    config.vm.network "forwarded_port", guest: 8080, host: 8080
    config.vm.network "forwarded_port", guest: 9080, host: 9080
    config.vm.network "private_network", ip: "192.168.77.21"

    config.ssh.forward_agent = true

    config.vm.synced_folder "./tomleo", "/home/vagrant/tomleo/", :nfs => true
    config.vm.synced_folder "./config", "/home/vagrant/config/", :nfs => true

    config.vm.provider "virtualbox" do |vb|
        vb.gui = false
        vb.customize ["modifyvm", :id, "--memory", "1920"]
        vb.customize ["modifyvm", :id, "--cpus", "4"]
    end

   config.vm.provision "ansible" do |ansible|
       ansible.playbook = "./provision/site.yml"
       #ansible.inventory_path = "./provision/hosts"
       ansible.verbose = "v"
       ansible.limit = 'all'
   end

end
