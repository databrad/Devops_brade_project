  Vagrant.configure("2") do |config|
    # Use Ubuntu as the base box
    config.vm.box = "ubuntu/focal64"
    # config.vm.box_version = "2022.10.18"
    # config.vm.box_download_insecure = true
  
    # Set up a synced folder to share the project code with the VM
    config.vm.synced_folder "./app", "/vagrant/app", type: "virtualbox", mount_options: ["dmode=777", "fmode=666"]

  
    # Define VM resources
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"
      vb.cpus = 4
    end
  
    # Configure the VM network
    config.vm.network "forwarded_port", guest: 5000, host: 5000, protocol: "tcp", auto_correct: true  # Flask app
  
    # Provision the VM using Ansible
    config.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "provisioning/playbook.yml"
      ansible.tags = ["common", "database", "backend"]
      ansible.verbose = "vvv"
    end
  end
  