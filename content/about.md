---
title: "About"
Description: "Making the Complex Simple and Easy to Understand!"
layout: "about"
---

{{< rawhtml >}}
<div style="display: flex; justify-content: center; width: 100%">
    <img src="https://avatars.githubusercontent.com/u/38770072?v=4" style="object-fit: cover; border-radius: 50%; width: 150px;" />
</div>
{{< /rawhtml >}}

# About me
I am currently a high school student, aspiring to become a computer engineer. I am self-taught and primarily experienced in C, C++, and Assembly (x86/64). I am passionate for low level development and machine learning.

# Projects
Here is a list of all of my *public* projects, including a short description for each one.

# 🖥️ SharedGL: OpenGL for VMs
An OpenGL implementation across networks and shared memory, enabling 3D acceleration in virtual machines and across devices on LAN. This project was created with the sole intention of achieving 3D acceleration inside of Windows guests running in QEMU, as previously there has been little to no support for graphics acceleration in these VMs, excluding full GPU passthrough. However, with the addition of networking, this has expanded from virtual machines to machines across a network. SharedGL offers an installable OpenGL client for both Linux and Windows, acting as the sole GPU driver.
 - [Source code](https://github.com/dmaivel/sharedgl)

# 🚀 vscc: x86 compiler backend
An experimental, lightweight, fast x86-64 compiler backend library, with no dependencies, written in C99, with the ability generate isolated bytecode, compliant with the SYS-V ABI. The primary motivator for this project was to further research/study the x86 instruction set and its intricate encoding model. It features its own intermediate language, assembler, and optimizer.
 - [Source code](https://github.com/dmaivel/vscc)

# 🐍 pyvscc: compile python to x86
An experimental, no dependencies, python compiler for the x86-64 architecture on Linux, utilizing `vscc` for JIT bytecode generation. The motivation behind this project was to provide a working example to show `vscc`'s features and functionality. It's quite basic and lagely unfinished, meaning it can only compile basic examples.
 - [Source code](https://github.com/dmaivel/pyvscc)

# 🧠 cml: neural network
A basic neural network implementation written in C. The motivation behind this project was to introduce myself to and research the basics of machine learning algorithms. The project provides a basic framework to train a model, get output from that model, save that model, and load that model again later.
 - [Source code](https://github.com/dmaivel/cml)

# ☁️ umvirt: usermode virtualization
Proof of concept for "virtualization" within usermode on x86-64, allowing users to execute priveledged code outside of the kernel space. This project is fairly small as it serves to be an example for the information discussed in one of my blog posts.
 - [Source code](https://github.com/dmaivel/umvirt)
 - [Blog post](../posts/virtualization-in-usermode)