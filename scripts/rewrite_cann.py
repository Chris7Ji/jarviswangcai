import re

html_path = "/Users/jiyingguo/.openclaw/workspace/jiaviswangcai.ai/article_ascend_cann.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_body = """
            <div class="post-body">
                <div class="summary-box" style="background: #F8FBFC; border-left: 4px solid var(--accent-blue); padding: 1.5rem; margin-bottom: 2rem; border-radius: 4px;">
                    <h3 style="margin-top: 0; color: var(--accent-blue);">📑 核心摘要</h3>
                    <p style="margin-bottom: 0;">要想真正发挥华为昇腾（Ascend）芯片的极致算力，仅停留在 PyTorch/MindSpore 框架层是远远不够的。针对 Gitee/GitCode 开源社区中的 CANN 仓库、工具链及项目实践，本文将带你<strong>自底向上</strong>穿透整个昇腾技术栈。通过对源码、项目示例的深度剖析，详细解答<strong>计算图融合流程、HCCL与AOE的协同关系、算子切分（Tiling）与循环展开策略，以及如何突破人工调优极限</strong>等硬核问题。</p>
                </div>

                <h2>一、 底层基石：达芬奇架构（Da Vinci）与 NPU 硬件</h2>
                <p>昇腾芯片（如 Ascend 910B）算力强悍的秘密，在于其专为神经网络设计的 <strong>达芬奇架构（Da Vinci Architecture）</strong>。在 NPU 内部，最小的物理计算单元是 <strong>AI Core</strong>。</p>
                
                <h3>1. AI Core 的三驾马车：Cube、Vector 与 Scalar</h3>
                <ul>
                    <li><strong>Cube Unit（矩阵乘单元）：</strong> NPU 的绝对算力担当。它专门执行 3D 的矩阵乘加运算，每次计算处理 16x16 的矩阵块（这就是为什么昇腾底层极其偏爱 <code>NC1HWC0</code> 数据格式，其中 C0=16）。</li>
                    <li><strong>Vector Unit（向量计算单元）：</strong> 负责 1D 向量的高效运算（如激活函数 ReLU、Sigmoid，张量的 Add/Mul 等 Element-wise 操作）。</li>
                    <li><strong>Scalar Unit（标量单元）：</strong> 相当于微型 CPU，负责地址流转、循环控制和分支判断。</li>
                </ul>

                <h3>2. 打破内存墙：极端的内存层级与 MTE 引擎</h3>
                <p>NPU 算力极高，如果不解决“喂数据”的问题，算力就会闲置。达芬奇架构设计了严密的内存层级，并配备了专门的搬砖工——<strong>MTE（Memory Transfer Engine）</strong>：</p>
                <ul>
                    <li><strong>Global Memory（HBM/DDR）：</strong> 容量大但延迟高。</li>
                    <li><strong>Unified Buffer (UB，统一缓冲区)：</strong> AI Core 内部极关键的私有高速内存。所有的 Vector 运算都必须在 UB 中进行。</li>
                    <li><strong>L1 Buffer：</strong> 用于数据复用，连接 Global Memory 和 Cube 单元。</li>
                </ul>
                <p>MTE 被细分为 MTE1（Global -> L1）、MTE2（Global/L1 -> UB 等）和 MTE3（UB -> Global）。MTE 的存在使得数据搬移独立于计算逻辑，为软件层的异步掩盖提供了硬件基础。</p>

                <hr style="margin: 2rem 0; border: 0; border-top: 1px dashed var(--border-color);">

                <h2>二、 承上启下：AscendOS 驱动层与 Runtime 层深度剖析</h2>
                <p>硬件之上，是昇腾的驱动层（Driver）与运行时环境（Runtime）。这一层起着关键的承上启下作用，将框架层的高级指令转化为底层硬件可执行的机器码。阅读 CANN 开源仓的 ACL（AscendCL）部分源码，我们可以清晰地看到它的运作机理。</p>
                
                <h3>1. Host 与 Device 的分离与协同</h3>
                <p>昇腾采用了 Host-Device 架构。Host（通常是 x86 或 ARM CPU）负责业务逻辑调度，Device（NPU）负责高强度计算。Host 下发任务并不是直接控制 NPU 寄存器，而是将 Task（任务）打包送入 PCIe 硬件队列。Device 侧的 Task Scheduler 轮询队列，将任务分配给空闲的 AI Core。</p>

                <h3>2. Context 与 Stream：多任务调度的灵魂</h3>
                <p>在 Runtime 层，有两个核心概念：</p>
                <ul>
                    <li><strong>Context（上下文）：</strong> 管理 Device 侧的生命周期、显存资源分配。每次调用前必须 <code>aclrtSetCurrentContext</code>。</li>
                    <li><strong>Stream（执行流）：</strong> 一个 Stream 就是一个严格串行执行的任务队列。不同 Stream 之间的任务是可以并发的。通过 <code>aclrtCreateStream</code>，我们可以实现 CPU 与 NPU 的异步，或者 MTE 数据搬移与 Cube 计算的异步（Overlap）。</li>
                </ul>
                <p><em>伪代码流程：</em></p>
                <pre><code>// 典型的 Runtime 层异步调度流程
aclrtStream stream;
aclrtCreateStream(&amp;stream);
// 异步发起内存拷贝 (Host -&gt; Device)
aclrtMemcpyAsync(devPtr, size, hostPtr, size, ACL_MEMCPY_HOST_TO_DEVICE, stream);
// 异步下发算子执行任务 (不会阻塞 Host)
aclopExecuteV2(opType, numInputs, inputDesc, inputs, numOutputs, outputDesc, outputs, attr, stream);
// 同步等待流中的任务全部完成
aclrtSynchronizeStream(stream);</code></pre>

                <hr style="margin: 2rem 0; border: 0; border-top: 1px dashed var(--border-color);">

                <h2>三、 CANN 软件中枢：Ascend C 算子开发与流水线并发</h2>
                <p>深入 Gitee/GitCode 上的 <code>ascend/samples</code> 库，你会发现 <strong>Ascend C</strong> 采用了 <code>SPMD (Single Program Multiple Data)</code> 编程模型。开发者只需编写单核逻辑，底层会自动将其映射到多个 AI Core 上并行。</p>

                <h3>双缓冲（Double Buffering）与流水线隐藏延迟</h3>
                <p>为了进一步压榨算力，Ascend C 引入了 <code>TPipe</code> 和 <code>TQue</code> 的概念，用来实现指令级的流水线（Pipeline）。</p>
                <p>假设我们把 <code>TQue</code> 深度设为 2（即 Ping-Pong 缓冲）。当 Vector 单元正在计算 Ping 缓冲的数据时，MTE 引擎可以同时从 Global Memory 将下一批数据搬运到 Pong 缓冲中。<strong>计算与搬运完全重叠，从而完美隐藏了内存读取延迟。</strong></p>

                <hr style="margin: 2rem 0; border: 0; border-top: 1px dashed var(--border-color);">

                <h2>四、 计算图与融合引擎：GE & FE 的极限压榨机制</h2>
                <p>当 PyTorch 框架下发一张复杂的计算图时，如果逐个执行算子，每算完一步都要把结果写回 Global Memory，内存带宽会立刻成为瓶颈。这就需要 <strong>GE (Graph Engine, 图引擎)</strong> 和 <strong>FE (Fusion Engine, 融合引擎)</strong> 出马。</p>

                <h3>FE 的 UB 融合 (Unified Buffer Fusion) 是怎么操作的？</h3>
                <p>FE 负责图级优化、算子复用和编译期融合。以最典型的 <code>Conv2D -&gt; BatchNorm -&gt; ReLU</code> 为例，其融合流程如下：</p>
                <ol>
                    <li><strong>模式匹配 (Pattern Matching)：</strong> FE 遍历计算图，发现连续的算子符合内置的融合规则（如 L1 Fusion、UB Fusion）。</li>
                    <li><strong>内存分配改写：</strong> FE 修改算子的输入输出依赖。原本 <code>Conv2D</code> 的输出指向 Global Memory，FE 将其改为直接指向 AI Core 内部的 <strong>Unified Buffer (UB)</strong>。</li>
                    <li><strong>AST 语法树合并：</strong> 将三个算子的底层实现逻辑合并为一棵 AST（抽象语法树），生成一个超级算子（Super Kernel）。</li>
                    <li><strong>执行期收益：</strong> 数据从 Global Memory 读入后，在 UB 内部连续完成卷积、归一化和激活，<strong>最后只写回 Global Memory 一次</strong>。这使得外存读写次数降低了近 70%。</li>
                </ol>

                <hr style="margin: 2rem 0; border: 0; border-top: 1px dashed var(--border-color);">

                <h2>五、 分布式通信与调优：HCCL 与 AOE 到底是什么关系？</h2>
                <p>在大模型时代，分布式训练是刚需。在 CANN 中，<strong>HCCL（集合通信库）</strong>和 <strong>AOE（自动调优引擎）</strong> 是一对互补的战友，但它们的职责完全不同。</p>

                <h3>1. HCCL：分布式通信的“肌肉”</h3>
                <p>HCCL 相当于 NVIDIA 的 NCCL。它提供 <code>AllReduce</code>、<code>AllGather</code>、<code>ReduceScatter</code> 等通信原语。HCCL 的优势在于其<strong>拓扑感知能力</strong>：</p>
                <ul>
                    <li><strong>节点内：</strong> 走 HCCS（Huawei Cache Coherent System）高速总线，建立 Ring（环形）或 Tree 拓扑。</li>
                    <li><strong>节点间：</strong> 走 RoCE v2（RDMA over Converged Ethernet），绕过 CPU 直接进行显存到显存的网络传输。</li>
                </ul>

                <h3>2. AOE 与 HCCL 的协同关系</h3>
                <p>如果说 HCCL 是肌肉，那么 <strong>AOE 就是大脑</strong>。HCCL 提供了通信能力，但“什么时候通信”、“怎么把通信耗时掩盖在计算里”则需要调优。AOE 包含算子调优（Operator Tuning）和子图调优（Subgraph Tuning）。<br>
                <strong>协同关系：</strong> AOE 可以分析包含 HCCL 通信算子的计算图，自动寻找 <code>Comm-Compute Overlap</code>（通信与计算重叠）的最佳策略。例如，它能探测出在进行上一层矩阵乘法时，并行下发 HCCL 的 AllGather 任务是最佳时机，从而让整体通信耗时被完美隐藏。</p>

                <hr style="margin: 2rem 0; border: 0; border-top: 1px dashed var(--border-color);">

                <h2>六、 核心痛点解答：算子切分、循环展开与“人工瓶颈”的破局之道</h2>

                <h3>1. 算子切分（Tiling）选择多少合适？</h3>
                <p>Tiling 是解决“内存墙”的核心手段，即把庞大的 Tensor 切分成能塞进 UB 的小块。<br>
                <strong>策略建议：</strong> 切分的大小受到 <code>Available_UB_Size</code> 的严格限制。假设 AI Core 的 UB 为 256KB，你需要同时容纳双缓冲的输入 X、Y 和输出 Z。那么理论上的单次处理数据量 <code>Tile_Size = Available_UB / (2 * (sizeof(X) + sizeof(Y) + sizeof(Z)))</code>。同时，在多核场景下，总数据量必须均匀分配给例如 32 个或 40 个 AI Core（BlockDim），以防部分核心“饥饿”。切得太碎，MTE 搬运指令开销占比过大；切得太大，会导致 UB 溢出（OOM）。</p>

                <h3>2. 循环展开（Loop Unrolling）几层最好？</h3>
                <p>在 Ascend C 的标量（Scalar）控制流中，频繁的 <code>for</code> 循环会导致分支跳转，产生流水线气泡（Pipeline Bubble）。使用 <code>#pragma unroll</code> 可以把循环体平铺。<br>
                <strong>策略建议：</strong> 一般建议展开 <strong>2 层、4 层或 8 层</strong>。但这绝非越大越好！展开层数过多，会导致生成的机器码体积暴增，不仅会污染 <strong>I-Cache（指令缓存）</strong> 导致 Cache Miss，还会耗尽 Scalar 寄存器引发 Spill（寄存器溢出到内存）。</p>

                <h3>3. 人工经验无法达到理论极限，解决方案是什么？</h3>
                <p>面对庞大的参数空间（如无数种 Tiling 切分组合、各种 Unroll 层数），人工凭借经验写出的算子往往只能达到硬件性能的 60%-70%。要逼近 100% 理论极限，我们的策略建议如下：</p>

                <ol>
                    <li><strong>抛弃硬编码，拥抱 Auto-Tiling API：</strong><br>
                    在最新的 CANN 架构中，不要在代码里写死 <code>tileLength = 256</code>。Ascend C 提供了 <code>AutoTiling</code> 机制。在 Host 侧编写 Tiling 解析函数，获取当前实际运行的 NPU 硬件信息（910A/910B 的 UB 大小不同），通过库函数动态计算最佳切分块，打包成结构体传给 Device 侧。</li>
                    
                    <li><strong>让机器训练机器（AOE 自动调优）：</strong><br>
                    当人工无法找到最优解时，引入 <strong>AOE (Auto Optimization Engine)</strong>。AOE 内部集成了基于 XGBoost、强化学习（RL）和遗传算法的搜索空间引擎。在部署阶段，开启 <code>--auto_tune_mode=RL</code>，AOE 会在真实硬件上自动编译、运行成千上万种 Tiling 与 Unrolling 参数的组合，监控耗时，并最终生成一份最优的 <code>knowledge_base.bin</code>。以后系统再遇到类似算子，直接查表应用最优参数。</li>
                    
                    <li><strong>数据格式降维打击（Format Optimization）：</strong><br>
                    比起在标量循环里死磕，不如在数据流转上做文章。尽量使用 <code>NC1HWC0</code> 的 5D 数据排布格式。由于 Cube 单元计算的基础矩阵块是 16x16，<code>C0=16</code> 的设计使得数据在被喂进 Cube 时天然对齐，彻底消灭了内部的 Padding（补零）和对齐开销。</li>
                </ol>

                <div style="margin-top: 3rem; padding-top: 1rem; border-top: 1px dashed var(--border-color); font-size: 0.9rem; color: var(--text-secondary);">
                    <p><em>📚 官方技术考证与参考学习链接：</em></p>
                    <ul style="list-style-type: none; padding-left: 0; margin-top: 0.5rem; line-height: 1.8;">
                        <li>[1] <strong>昇腾 CANN 官方首页：</strong> <a href="https://www.hiascend.com/zh/software/cann" target="_blank" style="color: var(--accent-blue); text-decoration: underline;">https://www.hiascend.com/zh/software/cann</a></li>
                        <li>[2] <strong>Ascend C 算子开发指南：</strong> <a href="https://www.hiascend.com/document/detail/zh/canncommercial/80RC1/operatordev/ascendcopdevg/ascendcopdevg_0001.html" target="_blank" style="color: var(--accent-blue); text-decoration: underline;">https://www.hiascend.com/document/detail/zh/canncommercial/80RC1/operatordev/ascendcopdevg/ascendcopdevg_0001.html</a></li>
                        <li>[3] <strong>AscendCL 应用开发指南：</strong> <a href="https://www.hiascend.com/document/detail/zh/canncommercial/80RC1/appdevg/aclcppdevg/aclcppdevg_000000.html" target="_blank" style="color: var(--accent-blue); text-decoration: underline;">https://www.hiascend.com/document/detail/zh/canncommercial/80RC1/appdevg/aclcppdevg/aclcppdevg_000000.html</a></li>
                        <li>[4] <strong>昇腾开源代码仓 (Gitee/GitCode)：</strong> <a href="https://gitee.com/ascend" target="_blank" style="color: var(--accent-blue); text-decoration: underline;">https://gitee.com/ascend</a> | <a href="https://gitcode.com/ascend" target="_blank" style="color: var(--accent-blue); text-decoration: underline;">https://gitcode.com/ascend</a></li>
                    </ul>
                </div>
            </div>
"""

prefix = content.split('<div class="post-body">')[0]
suffix = content.split('</div>\n            \n            <div class="post-nav">')[1]

new_content = prefix + new_body + '\n            <div class="post-nav">' + suffix

with open(html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("HTML rewritten successfully.")
