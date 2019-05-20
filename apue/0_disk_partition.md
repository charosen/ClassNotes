<h1>Linux下的磁盘分区和逻辑卷</h1>

<h2>一、硬盘接口类型</h2>

　　硬盘的接口主要有IDE、SATA、SCSI 、SAS和光纤通道等五种类型。其中IDE和SATA接口硬盘多用于家用产品中，也有部分应用于服务器，SATA是一种新生的硬盘接口类型，已经取代了大部分IDE接口应用。SCSI 、SAS主要应用于服务器上，普通家用设备一般不支持SCSI和SAS接口。SAS也是是一种新生的硬盘接口类型，可以和SATA以及部分SCSI设备无缝结合。光纤通道最初设计也不是为了硬盘设计开发的接口，是专门为网络系统设计的，但随着存储系统对速度的需求，才逐渐应用到硬盘系统中，并且其只应用在高端服务器上价格昂贵。

<h2>二、硬盘和分区</h2>

 　　Linux中主要有两种分区类型，分别为MBR（Master Boot Record）和GPT（GUID Partition Table），是在磁盘上存储分区信息的两种不同方式。这些分区信息包含了分区从哪里开始的信息，这样操作系统才知道哪个扇区是属于哪个分区的，以及哪个分区是可以启动的。在磁盘上创建分区时，你必须在MBR和GPT之间做出选择。
　　在Linux中会把设备映射成为一个/dev目录下的系统文件，IDE接口类型的硬盘设备映射的文件名称前缀为“hd”，SCSI、SATA、SAS等接口的硬盘设备映射的文件名称前缀为“sd”（部分虚拟机或者云主机的名称可能是其他的，比如“vd”），后面拼接从“a”开始一直到“z”用来区分不同的硬盘设备，在硬盘名称后面拼接数字形式的分区号用来区分不同的分区。

<h3>1、MBR分区</h3>

　　MBR的意思是“主引导记录”，它是存在于驱动器开始部分的一个特殊的启动扇区。这个扇区包含了已安装的操作系统的启动加载器和驱动器的逻辑分区信息。MBR支持最大2TB磁盘，它无法处理大于2TB容量的磁盘。MBR格式的磁盘分区主要分为**主分区（primary partion）**和**扩展分区（extension partion）**两种（**主分区**和扩展分区下的**逻辑分区**。主分区总数不能大于4个，其中最多只能有一个扩展分区。且住分区可以马上被挂载使用但不能再分区，扩展分区必须再进行二次分区后才能挂载。扩展分区下的二次分区被称之为逻辑分区，逻辑分区数量限制视磁盘类型而定。
　　
　　MBR的主分区号为1-4，逻辑分区号为从5开始累加的数字。比如设备主板上装了4块硬盘，分别为2块IDE接口硬盘，1块SCSI接口硬盘和一块SATA接口硬盘。其中2块IDE接口硬盘的分区策略为2个主分区和2个逻辑分区，SCSI分区策略为3个主分区和3个逻辑分区，SATA分区策略为4个主 分区。硬盘文件和分区名称如下：
　　
<table style="border-color: #999999; border-width: 0px; background-color: #eeeeee; width: 100%; border-style: solid;" border="0" frame="border" align="center">
<tbody>
<tr>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">硬盘</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;主分区1</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">主分区2</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">主分区3</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;主分区4</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;逻辑分区1</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;逻辑分区2</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;逻辑分区3</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">......</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">&nbsp;逻辑分区n</span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-size: 12px;">IDE1</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hda</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hda1(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hda2(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hda3(e)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hda5(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hda6(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">......</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-size: 12px;">IDE2</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hdb</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hdb1(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hdb2(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hdb3(e)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hdb5(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/hdb6(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">......</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
</tr>
<tr>
<td style="text-align: center;"><span style="font-size: 12px;">SCSI</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda1(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda2(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda3(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda4(e)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda5(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda6(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sda7(l)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">......</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>












</tr>
<tr>
<td style="text-align: center;"><span style="font-size: 12px;">SATA</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sdb</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sdb1(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sdb2(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sdb3(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/dev/sdb4(p)</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">......</span></td>
<td style="text-align: center;"><span style="font-size: 12px;">/</span></td>
</tr>
</tbody>
</table>


　　其中分区名称后面的（p）代表基本分区，（e）代表扩展分区，（l）代表逻辑分区。需要注意的是，如果分区策略中存在逻辑分区，则说明一定会有扩展分区，那么基本分区数则最多只能有3个，扩展分区数最多只能是1个，如果没有扩展分区则可以创建4个基本分区。想要创建逻辑分区，则必须先将唯一的扩展分区创建出来，并且如果删除了扩展分区，那么它下面的所有逻辑分区也会被自动删除。
　　
　　如果是SCSI接口硬盘则最多只能有15（其中扩展分区不能直接使用所以不计算）个分区，其中主分区最多4个，逻辑分区最多12个。IDE接口硬盘最多只能有63（其中扩展分区不能直接使用所以不计算）个分区，其中主分区最多4个，逻辑分区最多60个。

　　
<h3>2、GPT分区</h3>

　　GPT意为GUID分区表，驱动器上的每个分区都有一个全局唯一的标识符（globally unique identifier，GUID）。支持的最大磁盘可达18EB，它没有主分区和逻辑分区之分，每个硬盘最多可以有128个分区，具有更强的健壮性与更大的兼容性，并且将逐步取代MBR分区方式。GPT分区的命名和MBR类似，只不过没有主分区、扩展分区和逻辑分区之分，分区号直接从1开始累加一直到128。
　　
　　
<h2>三、逻辑卷</h2>

　　LVM（逻辑卷）的产生是因为传统的分区一旦分区好后就无法在线扩充空间，也存在一些工具能实现在线扩充空间但是还是会面临数据损坏的风险；传统的分区当分区空间不足时，一般的解决办法是再创建一个更大的分区将原分区卸载然后将数据拷贝到新分区，但是在企业的生产系统往往不允许停机或者允许停机的时间很短，LVM就能很好的解决在线扩充空间的问题，而且不会对数据造成影响，LVM还能通过快照在备份的过程中保证日志文件和表空间文件在同一时间点的一致性。
　　
　　在LVM中PE(Physical Extend)是卷的最小单位，默认4M大小，就像我们的数据是以页的形式存储一样，卷就是以PE的形式存储。PV(Physical Volume)是物理卷，如果要使用逻辑卷，首先第一步操作就是将物理磁盘或者物理分区格式化成PV，格式化之后PV就可以为逻辑卷提供PE了。VG(Volume Group)是卷组，VG就是将很多PE组合在一起生成一个卷组，当然这里的PE是可以跨磁盘的，如果当前服务器磁盘空间不足就可以增加一个新磁盘对当前系统不会产生任何影响。LV(Logical Volume)是逻辑卷，逻辑卷最终是给用户使用的，前面几个都是为创建逻辑卷做的准备，创建逻辑卷的大小只要不超过VG剩余空间就可以。

<h2>四、文件系统</h2>

<p>  当硬盘分区被创建完成之后，还并不能直接挂载到目录上存储文件，需要选择合适的文件系统进行格式化。常见的分区类型有FAT32、FAT16、NTFS、HP-UX等，而专供Linux使用的主流的一些分区有ext2/3/4、physical volume (LVM) 、softwareRAID、swap、vfat、xfs等。其中：</p>
   
<p>  1、ext2/3/4：是适合Linux的文件系统类型，由于ext3文件系统多了日志记录功能，因此系统恢复起来更加快速，ext4是ext3的升级，效率更加高，因此建议使用默认类型ext4类型，而不要使用ext2/3；</p>
<p>  2、physical volume (LVM)：这是一种弹性调整文件系统大小的机制，即可以让文件系统变大或变小，而不改变原文件数据的内容，功能不错，但性能不佳。</p>
<p>  3、softwareRAID：利用Linux系统的特性，用软件仿真出磁盘阵列功能。</p>
<p>  4、swap：就是内存交换空间。由于swap并不会使用到目录树的挂载，因此用swap就不需要指定挂载点。</p>
<p>  5、vfat：同时被Linux与windows所支持的文件系统类型。如果主机硬盘同事存在windows和linux两种操作系统，为了进行数据交换，可以使用该文件系统。</p>
<p>  6、xfs：也是一个文件系统类型，在centos7中将被作为默认的文件系统类型，替换ext4。</p>

<h2>五、使用fdisk操作分区</h2>

　　本文主要以CentOS 7发行版的Linux作为实验，我们使用Fdisk工具来操作分区，Fdisk 是各种 Linux 发行版本中最常用的分区工具。
　　首先输入`disk -h`命令查看帮助信息：

```
[root@localnat201 ~]# fdisk -h
用法：
fdisk [选项] <磁盘> 更改分区表
fdisk [选项] -l <磁盘> 列出分区表
fdisk -s <分区> 给出分区大小(块数)

选项：
-b <大小> 扇区大小(512、1024、2048或4096)
-c[=<模式>] 兼容模式：“dos”或“nondos”(默认)
-h 打印此帮助文本
-u[=<单位>] 显示单位：“cylinders”(柱面)或“sectors”(扇区，默认)
-v 打印程序版本
-C <数字> 指定柱面数
-H <数字> 指定磁头数
-S <数字> 指定每个磁道的扇区数
```

从中我们可以看出，使用`fdisk -l`;命令可查看分区表信息：

```
[root@localnat201 ~]# fdisk -l

磁盘 /dev/sda：32.2 GB, 32212254720 字节，62914560 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0x000b1bc3

   设备 Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    62914559    30407680   8e  Linux LVM

磁盘 /dev/sdb：53.7 GB, 53687091200 字节，104857600 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


磁盘 /dev/mapper/cl-root：29.0 GB, 28982640640 字节，56606720 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节


磁盘 /dev/mapper/cl-swap：2147 MB, 2147483648 字节，4194304 个扇区
Units = 扇区 of 1 * 512 = 512 bytes
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
```

从中我们可以看出，有4个设备，分别为/dev/sda、/dev/sdb、/dev/mapper/cl-root、/dev/mapper/cl-swap。其中/dev/sda硬盘已经有2个分区分区为：/dev/sda1和/dev/sda2。/dev/mapper/cl-root和/dev/mapper/cl-swap两个设备是/dev/sda2分区创建的逻辑卷。这里的/dev/sdb硬盘设备并没有被分区，我们则是需要来操作这个硬盘，至于如何操作逻辑卷后面会讲到。


输入`fdisk /dev/sdb`命令，对/dev/sda硬盘的分区表进行操作：

```
[root@localnat201 ~]# fdisk /dev/sdb
欢迎使用 fdisk (util-linux 2.23.2)。

更改将停留在内存中，直到您决定将更改写入磁盘。
使用写入命令前请三思。

Device does not contain a recognized partition table
使用磁盘标识符 0xc72a6f6a 创建新的 DOS 磁盘标签。
```

我们输入"m"选项可以查看到帮助信息：

```
命令(输入 m 获取帮助)：m
命令操作
   a   toggle a bootable flag 切换可引导标志
   b   edit bsd disklabel 编辑BSD磁盘标签
   c   toggle the dos compatibility flag 切换DOS兼容性标志
   d   delete a partition 删除分区
   g   create a new empty GPT partition table 创建一个新的空GPT分区表
   G   create an IRIX (SGI) partition table 创建一个ILIX（SGI）分区表
   l   list known partition types 列出已知分区类型
   m   print this menu 打印此菜单
   n   add a new partition 添加新分区
   o   create a new empty DOS partition table 创建一个新的空DOS分区表
   p   print the partition table 打印分区表
   q   quit without saving changes 不保存更改退出
   s   create a new empty Sun disklabel 创建一个新的空太阳标签
   t   change a partition's system id 更改分区的系统ID
   u   change display/entry units 更改显示/输入单元
   v   verify the partition table 验证分区表
   w   write table to disk and exit 将表写入磁盘并退出
   x   extra functionality (experts only) 额外功能（仅专家）

命令(输入 m 获取帮助)：
```

从上面的帮助信息中，可以得知一些选项的用途。这里主要注意"d"、"n"、"q"、"g"、"w"等选项。首先要明确分区格式，fdisk默认的分区格式是msdos（mbr），在此可输入"g"选项，将分区格式修改为GPT，不过在修改完保存退出之后，在输入`fdisk /dev/sdb`;命令进入分区模式，会出现`WARNING: fdisk GPT support is currently new, and therefore in an experimental phase. Use at your own discretion.`信息，提示fdisk gpt分区是新的功能，目前还在实验阶段。所以如果要进行GPT分区，那么推荐使用`parted`命令，后面会介绍到。

那么首先输入"n"选项来开始创建分区：

```
命令(输入 m 获取帮助)：n
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): 
```


可以看到交互界面打印的信息，提示需要选择一个分区类型，"p":为基本分区（默认）；"e"：为扩展分区。在此我们选择"p"，创建一个基本分区：

```
Partition type:
p primary (1 primary, 0 extended, 3 free)
e extended
Select (default p): p
分区号 (2-4，默认 2)：
```

交互界面提示需要选择一个分区号，范围为2-4。由于已经存在了一个基本分区，所以只可选择2、3、4（默认2，顺序累加）。在此我们输入2：

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): p
分区号 (2-4，默认 2)：2
起始 扇区 (2099200-314572799，默认为 2099200)：
```

可以看到交互界面提示序号选择其实扇区，默认为剩余未被分配的最小扇区，推荐选择默认（直接点击回车）；

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): p
分区号 (2-4，默认 2)：2
起始 扇区 (2099200-314572799，默认为 2099200)：
将使用默认值 2099200
Last 扇区, +扇区 or +size{K,M,G} (2099200-314572799，默认为 314572799)：
```

交互界面提示，要输入需要分配的截止扇区，默认为未被分配的最小扇区，此处推荐默认（直接点击回车）：

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): p
分区号 (2-4，默认 2)：2
起始 扇区 (2099200-314572799，默认为 2099200)：
将使用默认值 2099200
Last 扇区, +扇区 or +size{K,M,G} (2099200-314572799，默认为 314572799)：
将使用默认值 314572799
分区 2 已设置为 Linux 类型，大小设为 149 GiB

命令(输入 m 获取帮助)：
```

可以看到又回到了最初的交互界面，这表示分区表已经设置成功，输入选项q表示要放弃本次分区表的修改并退出，w选项表示保存本次分区表的修改并退出，此处选择w表示将分区信息写入到磁盘，此次分区完成；

回到最初操作分区表的地方，选择"d"选项，删除分区的功能：

```
命令(输入 m 获取帮助)：d
分区号 (1,2，默认 2)：
```

交互界面提示输入要删除的分区的分区号，此处选择2：

```
命令(输入 m 获取帮助)：d
分区号 (1,2，默认 2)：2
分区 2 已删除

命令(输入 m 获取帮助)：
```

交互界面提示本次分区表操作成功，输入选项"w"，表示将分区信息写入到磁盘，此次删除分区完成。回到最初选择分区类型的地方，选择"e"，创建扩展分区：

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): e
分区号 (2-4，默认 2)：
```

交互界面提示要输入扩展分区的分区号，可选范围为2-4，此处选择2：

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): e
分区号 (2-4，默认 2)：2
起始 扇区 (2099200-314572799，默认为 2099200)：
```

交互界面提示输入要分配给扩展分区的起始扇区，此处选择默认：

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): e
分区号 (2-4，默认 2)：2
起始 扇区 (2099200-314572799，默认为 2099200)：
将使用默认值 2099200
Last 扇区, +扇区 or +size{K,M,G} (2099200-314572799，默认为 314572799)：
```


交互界面提示输入要分配给扩展分区的截止扇区，此处选择默认：

```
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): e
分区号 (2-4，默认 2)：2
起始 扇区 (2099200-314572799，默认为 2099200)：
将使用默认值 2099200
Last 扇区, +扇区 or +size{K,M,G} (2099200-314572799，默认为 314572799)：
将使用默认值 314572799
分区 2 已设置为 Extended 类型，大小设为 149 GiB

命令(输入 m 获取帮助)：
```


交互界面提示本次对分区表的操作已完成，输入"w"选项，保存本次对分区表的操作；当再次创建分区的时候，交互界面就会将扩展分区的选项"e"替换成为逻辑分区的选项"l"：

```
Partition type:
   p   primary (1 primary, 1 extended, 2 free)
   l   logical (numbered from 5)
Select (default p): 
```

之后再要创建逻辑分区和之前创建分区的步骤一直，分区完成。至此CentOS中的分区操作已完成；接下来我们需要将物理分区格式化成某一个文件系统，我们使用mkds进行分区格式化操作，输入`mkfs -h`命令获取帮助信息：

```
[root@localhost ~]# mkfs -h
用法：
 mkfs [选项] [-t <类型>] [文件系统选项] <设备> [<大小>]

选项：
 -t, --type=<类型>  文件系统类型；
     fs-options     实际文件系统构建程序的参数
     <设备>         要使用设备的路径
     <大小>         要使用设备上的块数
 -V, --verbose      解释正在进行的操作；
                      多次指定 -V 将导致空运行(dry-run)
 -V, --version      显示版本信息并退出
                      将 -V 作为 --version 选项时必须是惟一选项
 -h, --help         显示此帮助并退出

更多信息请参阅 mkfs(8)。
```

从帮助信息中我们可以看到，可以使用`mkfs -t xfs /dev/sdb1 `进行格式化分区：

```
[root@localnat201 ~]# mkfs -t xfs /dev/sda2 
meta-data=/dev/sdb1              isize=512    agcount=4, agsize=624936 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0, sparse=0
data     =                       bsize=4096   blocks=2499744, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
```

格式化成xfs时，若提示分区已存在文件系统，则需要在分区前面加上-f选项强行覆盖，例如`mkfs -t xfs -f /dev/sda2`。被格式化的设备既可以是分区，也可以是逻辑卷。要查看所有分区的文件系统格式则可以使用`df -Th`命令。至此格式化分区完成。分区格式化完成之后则可以将分区挂载到某一个目录下面，正式开始使用改分区，我们在系统中创建一个用户挂载分区的目录：

```
[root@localhost ~]# mkdir /data
```

将分区挂载到目录上：

```
mount /dev/sda2 /data/
```

设置开机自动挂载分区到挂载点，编辑`vim /etc/fstab`

```
#
# /etc/fstab
# Created by anaconda on Sun Jun 25 07:16:25 2017
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
UUID=eb697457-a097-4263-8bbf-a75aa632d27c /                       ext4    defaults        1 1

/dev/sda2                               /data                   xfs    defaults        0 0
```


如果想要卸载挂载点：

```
[root@localnat201 ~]# umount /dev/sda2
```

至此挂载分区已完成；

<h2>六、使用parted操作分区</h2>

parted是一个可以分区并进行分区调整的工具，他可以创建，破坏，移动，复制，调整ext2 linux-swap fat fat32 reiserfs类型的分区，可以创建，调整，移动Macintosh的HFS分区，检测jfs，ntfs，ufs，xfs分区。既可以创建MBR分区，又可以用来创建GPT分区，如果你的硬盘大于2TB则必须要使用parted来创建GPT格式的分区。

可以使用`parted -h`命令查看使用说明

```
[root@localnat201 ~]# parted -h
Usage: parted [OPTION]... [DEVICE [COMMAND [PARAMETERS]...]...]
Apply COMMANDs with PARAMETERS to DEVICE.  If no COMMAND(s) are given, run in
interactive mode.

选项：
  -h, --help                      显示此求助信息
  -l, --list                      lists partition layout on all block devices 列出所有块设备上的分区布局
  -m, --machine                   displays machine parseable output 显示机器可分析输出
  -s, --script                    从不提示用户
  -v, --version                   显示版本
  -a, --align=[none|cyl|min|opt]  alignment for new partitions

命令：
  align-check TYPE N                        check partition N for TYPE(min|opt)
        alignment
  help [COMMAND]                           print general help, or help on
        COMMAND
  mklabel,mktable LABEL-TYPE               create a new disklabel (partition
        table)
  mkpart PART-TYPE [FS-TYPE] START END     make a partition
  name NUMBER NAME                         name partition NUMBER as NAME
  print [devices|free|list,all|NUMBER]     display the partition table,
        available devices, free space, all found partitions, or a particular
        partition
  quit                                     exit program
  rescue START END                         rescue a lost partition near START
        and END
  rm NUMBER                                delete partition NUMBER
  select DEVICE                            choose the device to edit
  disk_set FLAG STATE                      change the FLAG on selected device
  disk_toggle [FLAG]                       toggle the state of FLAG on selected
        device
  set NUMBER FLAG STATE                    change the FLAG on partition NUMBER
  toggle [NUMBER [FLAG]]                   toggle the state of FLAG on partition
        NUMBER
  unit UNIT                                set the default unit to UNIT
  version                                  display the version number and
        copyright information of GNU Parted

Report bugs to bug-parted@gnu.org
```


从帮助信息中可看出，使用`parted -l`命令可查看分区表信息：

```
[root@localnat201 ~]# parted -l
Model: VMware, VMware Virtual S (scsi)
Disk /dev/sda: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  标志
     1049kB  1075MB  1074MB  primary  xfs          启动
     1075MB  32.2GB  31.1GB  primary               lvm


错误: /dev/sdb: unrecognised disk label
Model: VMware, VMware Virtual S (scsi)                                    
Disk /dev/sdb: 107GB
Sector size (logical/physical): 512B/512B
Partition Table: unknown
Disk Flags: 

Model: Linux device-mapper (linear) (dm)
Disk /dev/mapper/cl-swap: 2147MB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Fla　　gs: 

Number  Start  End     Size    File system     标志
     0.00B  2147MB  2147MB  linux-swap(v1)


Model: Linux device-mapper (linear) (dm)
Disk /dev/mapper/cl-root: 29.0GB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Flags: 

Number  Start  End     Size    File system  标志
     0.00B  29.0GB  29.0GB  xfs
```

从中可看出与上面`fdisk -l`命令返回的差不多的信息。总共有4个设备：/dev/sda和/dev/sdb为物理设备，/dev/mapper/cl-swap和/dev/mapper/cl-root为逻辑卷创建的设备。可以看到/dev/sdb还没有分区，并且还看到上面有一个错误信息`错误: /dev/sdb: unrecognised disk label`。这是由于该磁盘设备没有设置上标签（label）所以会有错误，只需要设置了标签就可以了。

这里我们使用`parted /dev/sdb`命令开始分区：

```
[root@localnat201 ~]# parted /dev/sdb 
GNU Parted 3.1
使用 /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) 
```

输入help选项，查看帮助信息：

```
[root@localnat201 ~]# parted /dev/sdb 
GNU Parted 3.1
使用 /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) help                                                             
  align-check TYPE N                        check partition N for TYPE(min|opt) alignment
  help [COMMAND]                           print general help, or help on COMMAND
  mklabel,mktable LABEL-TYPE               create a new disklabel (partition table)
  mkpart PART-TYPE [FS-TYPE] START END     make a partition
  name NUMBER NAME                         name partition NUMBER as NAME
  print [devices|free|list,all|NUMBER]     display the partition table, available devices, free space, all found partitions, or a particular partition
  quit                                     exit program
  rescue START END                         rescue a lost partition near START and END
  rm NUMBER                                delete partition NUMBER
  select DEVICE                            choose the device to edit
  disk_set FLAG STATE                      change the FLAG on selected device
  disk_toggle [FLAG]                       toggle the state of FLAG on selected device
  set NUMBER FLAG STATE                    change the FLAG on partition NUMBER
  toggle [NUMBER [FLAG]]                   toggle the state of FLAG on partition NUMBER
  unit UNIT                                set the default unit to UNIT
  version                                  display the version number and copyright information of GNU Parted
(parted)
```


也可以在"help"选项后面加上具体的命令，可以查看具体命令的帮助信息；接下来使用`mklabel gpt`或者`mktable `命令格式化分区类型和设置标签：

```
[root@localnat201 ~]# parted /dev/sdb 
GNU Parted 3.1
使用 /dev/sdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) help                                                             
  align-check TYPE N                        check partition N for TYPE(min|opt) alignment
  help [COMMAND]                           print general help, or help on COMMAND
  mklabel,mktable LABEL-TYPE               create a new disklabel (partition table)
  mkpart PART-TYPE [FS-TYPE] START END     make a partition
  name NUMBER NAME                         name partition NUMBER as NAME
  print [devices|free|list,all|NUMBER]     display the partition table, available devices, free space, all found partitions, or a particular partition
  quit                                     exit program
  rescue START END                         rescue a lost partition near START and END
  rm NUMBER                                delete partition NUMBER
  select DEVICE                            choose the device to edit
  disk_set FLAG STATE                      change the FLAG on selected device
  disk_toggle [FLAG]                       toggle the state of FLAG on selected device
  set NUMBER FLAG STATE                    change the FLAG on partition NUMBER
  toggle [NUMBER [FLAG]]                   toggle the state of FLAG on partition NUMBER
  unit UNIT                                set the default unit to UNIT
  version                                  display the version number and copyright information of GNU Parted
(parted) mklabel gpt                                                      
(parted)
```


此处可选择modos（mbr）和gpt类型，如果修改的分区标签类型，则分区所有数据将会丢失；接下来可输入`print`选项，打印分区信息：

```
(parted) print                                                            
Model: VMware, VMware Virtual S (scsi)
Disk /dev/sdb: 107GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start  End  Size  File system  Name  标志

(parted)
```

由此可以看出分区已经是GPT分区格式；加下来需要创建分区，创建分区需要使用`mkpart`命令，在此我们可以输入`help mkpart`命令查看帮助信息：

```
(parted) help mkpart                                                      
  mkpart PART-TYPE [FS-TYPE] START END     make a partition

    分区类型是：primary（主分区）、logical（逻辑分区）、extended（扩展分区）之一
    文件系统类型是以下任意一项：btrfs, nilfs2, ext4, ext3, ext2, fat32, fat16, hfsx, hfs+, hfs, jfs, swsusp, linux-swap(v1), linux-swap(v0), ntfs, reiserfs, hp-ufs, sun-ufs, xfs, apfs2, apfs1, asfs, amufs5, amufs4,
        amufs3, amufs2, amufs1, amufs0, amufs, affs7, affs6, affs5, affs4, affs3, affs2, affs1, affs0, linux-swap, linux-swap(new), linux-swap(old)
        START and END are disk locations, such as 4GB or 10%.  Negative values count from the end of the disk.  For example, -1s specifies exactly the last sector.
        
        'mkpart' makes a partition without creating a new file system on the partition.  FS-TYPE may be specified to set an appropriate partition ID.
```


我们用`mkpart xfs 0 100`命令创建分区，xfs是文件系统类型（这里只是做说明或者说是分区的名称，分区完成之后是需要使用`mkfs`命令进行真正的格式化的，否则不能挂载）， 0是磁盘的起始位置，100%是磁盘的结束位置：

```
(parted) mkpart primary xfs 0 100%                                        
警告: The resulting partition is not properly aligned for best performance.
忽略/Ignore/放弃/Cancel?
```

创建的过程中，我们会看到有警告信息`The resulting partition is not properly aligned for best performance.`，说分区没有正确对齐，会影响最佳新能。这里说的是磁盘的位置没有给一个合适的值。其实在使用fdisk分区的时候，会有默认的起始和结束扇区，所以如果不是很确定这个值，那么可以先试用fdisk命令进入分区模式，看一下默认的起始扇区和结束扇区是多少。我这里的起始扇区是2048，但由于parted默认是M为位置单位，所以这里需要使用s说明是扇区为单位。结束扇还是100%，所以命令为`mkpart xfs 2048s 100`：

```
(parted) mkpart xfs 2048s 100%                                            
(parted)
```


其中不需要指明分区类型是主分区还是逻辑分区，GPT分区只有一种分区格式，如果是msdos（mbr）才需要指明。可以使用`rm 分区号`命令删除分区，使用`quit`命令退出当前分区模式，至此parted命令进行GPT分区已完成；格式化分区和挂载分区与上面fdisk分区中的方式一样。

<h2>七、使用逻辑卷</h2>

首先我们需要将物理设备（可以是物理磁盘/dev/sdb、也可以是物理分区/dev/sdb1）格式化为PV（物理卷），在此我们使用`parted -l`命令查看我们有哪些可供使用的物理设备：

```
[root@localnat201 ~]# parted -l
Model: VMware, VMware Virtual S (scsi)
Disk /dev/sda: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags: 

Number  Start   End     Size    Type     File system  标志
     1049kB  1075MB  1074MB  primary  xfs          启动
     1075MB  32.2GB  31.1GB  primary               lvm


Model: VMware, VMware Virtual S (scsi)
Disk /dev/sdb: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name  标志
     1049kB  21.5GB  21.5GB               xfs


错误: /dev/sdc: unrecognised disk label
Model: VMware, VMware Virtual S (scsi)                                    
Disk /dev/sdc: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: unknown
Disk Flags: 

Model: Linux device-mapper (linear) (dm)
Disk /dev/mapper/cl-swap: 2147MB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Flags: 

Number  Start  End     Size    File system     标志
     0.00B  2147MB  2147MB  linux-swap(v1)


Model: Linux device-mapper (linear) (dm)
Disk /dev/mapper/cl-root: 29.0GB
Sector size (logical/physical): 512B/512B
Partition Table: loop
Disk Flags: 

Number  Start  End     Size    File system  标志
     0.00B  29.0GB  29.0GB  xfs
```

这里我们抛开已经做过分区和已经存在的物理卷的一些设备，其中/dev/sdb和/dev/sdc这两个物理磁盘是需要我们关注的。我们可以看到/dev/sdb这块磁盘已经有了一个分区，分区号是1也就是/dev/sdb1分区（gpt分区表只展示分区号，只要将磁盘名称拼上分区号就是分区名称），而/dev/sdc磁盘并没有做过分区。所以我们首先需要使用`pvcreate`命令将/dev/sdb1和/dev/sdc格式化成PV：

```
[root@localnat201 ~]# pvcreate /dev/sdb1 /dev/sdc 
  Physical volume "/dev/sdb1" successfully created.
  Physical volume "/dev/sdc" successfully created.
[root@localnat201 ~]#
```

这里可以看到创建成功了，其中pvcreate是创建命令，后面参数是需要初始化的物理设备，多个设备之间使用空格分隔。我们可以使用`pvdisplay`命令或者`pvs`命令查看已经存在的PV信息：

```
[root@localnat201 ~]# pvcreate /dev/sdb1 /dev/sdc 
  Physical volume "/dev/sdb1" successfully created.
  Physical volume "/dev/sdc" successfully created.
[root@localnat201 ~]# clear
[root@localnat201 ~]# pvdisplay 
  --- Physical volume ---
  PV Name               /dev/sda2
  VG Name               cl
  PV Size               <29.00 GiB / not usable 3.00 MiB
  Allocatable           yes 
  PE Size               4.00 MiB
  Total PE              7423
  Free PE               1
  Allocated PE          7422
  PV UUID               KdNi7s-YftA-YY9W-hK7a-PHw1-j7n2-ln4cLg
   
  "/dev/sdc" is a new physical volume of "20.00 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sdc
  VG Name               
  PV Size               20.00 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               AbmsNB-2NUK-IxJA-QYY7-N81f-avOz-wyMKiR
   
  "/dev/sdb1" is a new physical volume of "<20.00 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sdb1
  VG Name               
  PV Size               <20.00 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               sts9D4-P47z-Qrj2-WaWX-9wEU-o8jo-Y70xgb
   
[root@localnat201 ~]# pvs
  PV         VG Fmt  Attr PSize   PFree  
  /dev/sda2  cl lvm2 a--  <29.00g   4.00m
  /dev/sdb1     lvm2 ---  <20.00g <20.00g
  /dev/sdc      lvm2 ---   20.00g  20.00g
```


如果有需要我们也可以使用`pvremove`命令删除物理卷：

```
[root@localnat201 ~]# pvremove /dev/sdc 
  Labels on physical volume "/dev/sdc" successfully wiped.
[root@localnat201 ~]# 
```

我们可以看到有三个设备已经被初始化成了PV，这里不需要关注/dev/sda2分区，这是在安装系统时自动初始化的PV，这里/dev/sdb1分区和/dev/sdc磁盘是我们这次初始化的PV。既然创建了PV那么就需要VG（PV组）了，下面我们来使用`vgcreate`命令来创建VG（卷组）：

```
[root@localnat201 ~]# vgcreate myvg /dev/sdb1 
  Volume group "myvg" successfully created
[root@localnat201 ~]#
```

可以看见已经创建成功，其中vgcreate是创建命令myvg是这个VG组的名称，/dev/sdb1是指将这个已经初始化成PV的设备添加套这个卷组中，如果需要添加多个设备使用空格分隔。我们可以使用`vgdisplay`或者`vgs`命令查看卷组信息：

```
[root@localnat201 ~]# vgdisplay 
  --- Volume group ---
  VG Name               cl
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  3
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               2
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <29.00 GiB
  PE Size               4.00 MiB
  Total PE              7423
  Alloc PE / Size       7422 / 28.99 GiB
  Free  PE / Size       1 / 4.00 MiB
  VG UUID               EZIlfD-2r61-x8RC-qLwl-Nsqp-D5zr-J8pPfI
   
  --- Volume group ---
  VG Name               myvg
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <20.00 GiB
  PE Size               4.00 MiB
  Total PE              5119
  Alloc PE / Size       0 / 0   
  Free  PE / Size       5119 / <20.00 GiB
  VG UUID               dVW1W5-AMKN-xMEy-TGBs-QRF7-Nvvs-ZnFpLd
   
[root@localnat201 ~]# vgs
  VG   #PV #LV #SN Attr   VSize   VFree  
  cl     1   2   0 wz--n- <29.00g   4.00m
  myvg   1   0   0 wz--n- <20.00g <20.00g
```

我们可以看到我们创建的名称为myvg的卷组，大小为小于20G，也就是说最大没有20G可用，PE大小是4M，有5119个PE。如果有需要我们可以使用`vgremove`命令删除卷组：

```
[root@localnat201 ~]# vgremove myvg
  Volume group "myvg" successfully removed
[root@localnat201 ~]#
```

有了卷组，接下来我们就可以真正开始创建逻辑卷了，这里使用`lvcreate -n 逻辑卷名称 -l 逻辑卷PE数 卷组名`命令来创建逻辑卷：

```
[root@localnat201 ~]# lvcreate -n mylv -l 5119  myvg
  Logical volume "mylv" created.
[root@localnat201 ~]# 
```

在这里可以看到名称为mylv的逻辑卷创建成功，其中`-l`选项可以换成`-L`，用来只用以磁盘大小为单位的数值，比如说K、M、G、T等。但是这里的VG可用大小是5119PE和小于20.0G，使用G做单位不知道具体小于多小，不好给定一个具体的值，所以这里我们使用PE作为单位。接下来我们可以使用`lvdisplay`或者`lvs`命令查看逻辑卷信息：

```
[root@localnat201 ~]# lvdisplay 
  --- Logical volume ---
  LV Path                /dev/cl/swap
  LV Name                swap
  VG Name                cl
  LV UUID                UzXXeu-TO2S-xXWF-ZZtt-Kq2L-JaAE-GLdRvQ
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2017-12-01 18:58:38 +0800
  LV Status              available
  # open                 2
  LV Size                2.00 GiB
  Current LE             512
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:1
   
  --- Logical volume ---
  LV Path                /dev/cl/root
  LV Name                root
  VG Name                cl
  LV UUID                emExFt-9Y5c-dEq7-2mPp-kiO0-03j4-4IxbsT
  LV Write Access        read/write
  LV Creation host, time localhost.localdomain, 2017-12-01 18:58:39 +0800
  LV Status              available
  # open                 1
  LV Size                26.99 GiB
  Current LE             6910
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:0
   
  --- Logical volume ---
  LV Path                /dev/myvg/mylv
  LV Name                mylv
  VG Name                myvg
  LV UUID                KloMrL-XW8i-Eo2J-pdI3-f28r-s4gw-wIBSfB
  LV Write Access        read/write
  LV Creation host, time localnat201, 2018-04-24 23:11:28 +0800
  LV Status              available
  # open                 0
  LV Size                <20.00 GiB
  Current LE             5119
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:2
   
[root@localnat201 ~]# lvs
  LV   VG   Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root cl   -wi-ao----  26.99g                                                    
  swap cl   -wi-ao----   2.00g                                                    
  mylv myvg -wi-a----- <20.00g
```


这里我们可以看到具体的逻辑卷信息了，我们创建的这个逻辑卷在操作系统中映射的文件的据对路径为"/dev/myvg/mylv"，但是一般逻辑卷会在"/dev/mapper"目录下面创建一个软连接"/dev/mapper/myvg-mylv"，软连接名称为卷组名称加-再加上逻辑卷名称。如果有必要我们可以使用`lvremove /dev/myvg/mylv`命令删除逻辑卷。这个逻辑卷和物理分区一样，需要先格式化成合适的文件系统，然后挂载到某一个目录上就可以了，格式化分区和挂载分区与上面fdisk分区中的方法一样:

```
[root@localnat201 ~]# mkfs -t xfs /dev/myvg/mylv 
meta-data=/dev/myvg/mylv         isize=512    agcount=4, agsize=1310464 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0, sparse=0
data     =                       bsize=4096   blocks=5241856, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
[root@localnat201 ~]# mount /dev/myvg/mylv /data/
[root@localnat201 ~]# df -lh
文件系统               容量  已用  可用 已用% 挂载点
/dev/mapper/cl-root     27G  5.6G   22G   21% /
devtmpfs               1.9G     0  1.9G    0% /dev
tmpfs                  1.9G     0  1.9G    0% /dev/shm
tmpfs                  1.9G  8.6M  1.9G    1% /run
tmpfs                  1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1             1014M  186M  829M   19% /boot
tmpfs                  378M     0  378M    0% /run/user/0
/dev/mapper/myvg-mylv   20G   33M   20G    1% /data
```

其中"/dev/mapper/myvg-mylv"是"/dev/myvg/mylv"的软连接，这两个路径都可以对逻辑卷进项操作，至此逻辑卷的创建和格式化挂载完成。这时如果由于逻辑卷空间满了需要扩充，我们可以使用`vgs`命令查看还有没有可供逻辑卷扩充的空间：

```
[root@localnat201 ~]# vgs
  VG   #PV #LV #SN Attr   VSize   VFree
  cl     1   2   0 wz--n- <29.00g 4.00m
  myvg   1   1   0 wz--n- <20.00g    0 
[root@localnat201 ~]# 
```

我们可以看到，名称为myvg的卷组的自由空间已经是0了，这个时候我们需要线扩充vg。这是我们可以使用`pvs`命令查看有没有可供vg扩充的pv：

```
[root@localnat201 ~]# pvs
  PV         VG   Fmt  Attr PSize   PFree 
  /dev/sda2  cl   lvm2 a--  <29.00g  4.00m
  /dev/sdb1  myvg lvm2 a--  <20.00g     0 
  /dev/sdc        lvm2 ---   20.00g 20.00g
```

这是我们看到/dev/sdc这个pv并没有被添加到某个vg中可以使用，我们使用`vgextend`命令扩充卷组：

```
[root@localnat201 ~]# vgextend myvg /dev/sdc 
  Volume group "myvg" successfully extended
[root@localnat201 ~]# vgdisplay 
  --- Volume group ---
  VG Name               cl
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  3
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               2
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <29.00 GiB
  PE Size               4.00 MiB
  Total PE              7423
  Alloc PE / Size       7422 / 28.99 GiB
  Free  PE / Size       1 / 4.00 MiB
  VG UUID               EZIlfD-2r61-x8RC-qLwl-Nsqp-D5zr-J8pPfI
   
  --- Volume group ---
  VG Name               myvg
  System ID             
  Format                lvm2
  Metadata Areas        2
  Metadata Sequence No  5
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                1
  Open LV               0
  Max PV                0
  Cur PV                2
  Act PV                2
  VG Size               39.99 GiB
  PE Size               4.00 MiB
  Total PE              10238
  Alloc PE / Size       5119 / <20.00 GiB
  Free  PE / Size       5119 / <20.00 GiB
  VG UUID               dVW1W5-AMKN-xMEy-TGBs-QRF7-Nvvs-ZnFpLd
```

我们可以看到VG扩充成功，并且已经有了5119PE的自由空间。现在我们就可以使用这个剩余空间扩充逻辑卷了，这里我们可以使用`lvextend`命令扩充逻辑卷：

```
[root@localnat201 ~]# lvextend -l +5119 /dev/myvg/mylv 
  Size of logical volume myvg/mylv changed from <20.00 GiB (5119 extents) to 39.99 GiB (10238 extents).
  Logical volume myvg/mylv successfully resized.
[root@localnat201 ~]# lvs
  LV   VG   Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root cl   -wi-ao---- 26.99g                                                    
  swap cl   -wi-ao----  2.00g                                                    
  mylv myvg -wi-a----- 39.99g                                                    
[root@localnat201 ~]# vgs
  VG   #PV #LV #SN Attr   VSize   VFree
  cl     1   2   0 wz--n- <29.00g 4.00m
  myvg   2   1   0 wz--n-  39.99g    0
[root@localnat201 ~]# df -lh
文件系统               容量  已用  可用 已用% 挂载点
/dev/mapper/cl-root     27G  5.6G   22G   21% /
devtmpfs               1.9G     0  1.9G    0% /dev
tmpfs                  1.9G     0  1.9G    0% /dev/shm
tmpfs                  1.9G  8.6M  1.9G    1% /run
tmpfs                  1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1             1014M  186M  829M   19% /boot
tmpfs                  378M     0  378M    0% /run/user/0
/dev/mapper/myvg-mylv   20G   33M   19.9G    1% /data
```


我们可以看到扩充逻辑卷成功，逻辑卷大小变成了39.9G了，而卷组剩余大小变成了0。但是这是如果我们直接将这个逻辑卷挂载到/data目录下面，再使用`df -lh`命令查看，你就会发现逻辑卷大小并没有发生变化，其实这是因为逻辑卷大小虽然扩充了，但是逻辑卷上面的文件系统并没有更新，所以需要先更新文件系统才能真正使用到扩充后的空间。注意这里使用`xfs_growfs /dev/myvg/mylv`命令更新一下文件系统，不能重新格式化整个分区的文件系统：

```
[root@localnat201 ~]# xfs_growfs /dev/m
mapper/ mcelog  mem     midi    mqueue/ myvg/   
[root@localnat201 ~]# xfs_growfs /dev/myvg/mylv 
meta-data=/dev/mapper/myvg-mylv  isize=512    agcount=4, agsize=1310464 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0 spinodes=0
data     =                       bsize=4096   blocks=5241856, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 5241856 to 10483712
[root@localnat201 ~]# df -lh
文件系统               容量  已用  可用 已用% 挂载点
/dev/mapper/cl-root     27G  5.6G   22G   21% /
devtmpfs               1.9G     0  1.9G    0% /dev
tmpfs                  1.9G     0  1.9G    0% /dev/shm
tmpfs                  1.9G  8.6M  1.9G    1% /run
tmpfs                  1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1             1014M  186M  829M   19% /boot
tmpfs                  378M     0  378M    0% /run/user/0
/dev/mapper/myvg-mylv   40G   33M   40G    1% /data
```


我们可以看到，已经挂载的逻辑卷大小达到了40G，说明扩充分区成功了。这里需要注意，由于我是用的是xfs的文件系统，所以使用`xfs_growfs`命令来更新文件系统，如果是ext2/ext3/ext4等文件系统则需使用`resize2fs`命令来更新文件系统了。如果觉得麻烦，在这里我们也可以直接使用`lvresize -l 2000 -r /dev/myvg/mylv`命令，可以替代`lvextend`和`xfs_growfs/resize2fs`命令，这里的大小如果前面有"+"号，则代表增加大小，如果没有"+"但是设置的值比原来的大则也是增加大小。　　

在平时我们不只是需要扩充逻辑卷，还有可能需要收缩（减小）或者卸载逻辑卷，注意xfs文件系统只支持增大分区空间的情况，不支持减小的情况，硬要减小的话，只能在减小后将逻辑分区重新通过mkfs.xfs命令重新格式化才能挂载上，这样的话这个逻辑分区上原来的数据就丢失了。但是ext文件系统可以支持减小减小逻辑卷操作，接下来我们做ext收缩逻辑卷操作。对逻辑卷进行收缩操作之前，如果逻辑卷已经挂载到了目录上必须先卸载逻辑卷的挂载，然后缩小文件系统，最后才是缩小逻辑卷，而且收缩的大小也不能超过剩余空间大小。

```
[root@localnat201 ~]# umount /dev/myvg/mylv 
[root@localnat201 ~]#
```

卸载了逻辑卷的挂载之后，需要先收缩文件系统，这一步一定是要在收缩逻辑卷之前操作，在这之前我已经将逻辑卷格式化成了ext4的盖世乐，所以这里我们使用`resize2fs`明来执行收缩操作：

```
[root@localnat201 ~]# resize2fs /dev/myvg/mylv 30G
resize2fs 1.42.9 (28-Dec-2013)
Resizing the filesystem on /dev/myvg/mylv to 7864320 (4k) blocks.
The filesystem on /dev/myvg/mylv is now 7864320 blocks long.

[root@localnat201 ~]#
```


然后将逻辑卷缩小：

```
[root@localnat201 ~]# lvreduce -L 30G /dev/myvg/mylv 
  WARNING: Reducing active logical volume to 30.00 GiB.
  THIS MAY DESTROY YOUR DATA (filesystem etc.)
Do you really want to reduce myvg/mylv? [y/n]: y
  Size of logical volume myvg/mylv changed from 39.99 GiB (10238 extents) to 30.00 GiB (7680 extents).
  Logical volume myvg/mylv successfully resized.
[root@localnat201 ~]# lvs
  LV   VG   Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root cl   -wi-ao---- 26.99g                                                    
  swap cl   -wi-ao----  2.00g                                                    
  mylv myvg -wi-a----- 30.00g                                                    
[root@localnat201 ~]#
```

这里缩小成功了，注意这里没有在30G前面加上减号，但是30G本来就比原来的40G要小，所以是缩小操作。接下来只要在挂载，那么本次缩小逻辑卷操作就完成了：

```
[root@localnat201 ~]# mount /dev/myvg/mylv /data/
[root@localnat201 ~]# df -Th
文件系统              类型      容量  已用  可用 已用% 挂载点
/dev/mapper/cl-root   xfs        27G  5.6G   22G   21% /
devtmpfs              devtmpfs  1.9G     0  1.9G    0% /dev
tmpfs                 tmpfs     1.9G     0  1.9G    0% /dev/shm
tmpfs                 tmpfs     1.9G  8.6M  1.9G    1% /run
tmpfs                 tmpfs     1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1             xfs      1014M  186M  829M   19% /boot
tmpfs                 tmpfs     378M     0  378M    0% /run/user/0
/dev/mapper/myvg-mylv ext4       30G   45M   28G    1% /data
[root@localnat201 ~]#
```


这里如果觉得麻烦，可以使`lvresize -l 30G -r /dev/vg2/xfstest`命令替代`lvextend`和`resize2fs`命令：

```
[root@localnat201 ~]# lvresize -L 20G -r /dev/myvg/mylv 
Do you want to unmount "/data"? [Y|n] y
fsck，来自 util-linux 2.23.2
/dev/mapper/myvg-mylv: 11/1966080 files (0.0% non-contiguous), 167453/7864320 blocks
resize2fs 1.42.9 (28-Dec-2013)
Resizing the filesystem on /dev/mapper/myvg-mylv to 5242880 (4k) blocks.

The filesystem on /dev/mapper/myvg-mylv is now 5242880 blocks long.

  Size of logical volume myvg/mylv changed from 30.00 GiB (7680 extents) to 20.00 GiB (5120 extents).
  Logical volume myvg/mylv successfully resized.
[root@localnat201 ~]# df -Th
文件系统              类型      容量  已用  可用 已用% 挂载点
/dev/mapper/cl-root   xfs        27G  5.6G   22G   21% /
devtmpfs              devtmpfs  1.9G     0  1.9G    0% /dev
tmpfs                 tmpfs     1.9G     0  1.9G    0% /dev/shm
tmpfs                 tmpfs     1.9G  8.6M  1.9G    1% /run
tmpfs                 tmpfs     1.9G     0  1.9G    0% /sys/fs/cgroup
/dev/sda1             xfs      1014M  186M  829M   19% /boot
tmpfs                 tmpfs     378M     0  378M    0% /run/user/0
/dev/mapper/myvg-mylv ext4       20G   45M   19G    1% /data
```
我们可以看到也缩小成功了，至此逻辑卷的操作也都已经完成。