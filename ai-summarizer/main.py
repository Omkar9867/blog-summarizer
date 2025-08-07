from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

article_text = """Article: The Evolution of Cloud Computing
Cloud computing has revolutionized the way businesses operate, offering scalable solutions for storage, computing power, and applications over the internet. The evolution of cloud computing can be traced back to the 1960s, but it gained massive popularity in the early 21st century. The journey can be broken down into three main phases: the introduction of the concept, the development of virtualized infrastructure, and the rise of hybrid cloud models.

Introduction to Cloud Computing (1960s-1990s):
The initial concept of cloud computing can be linked to time-sharing systems developed in the 1960s. These systems allowed multiple users to access a centralized computing power remotely. By the 1990s, the internet made it possible to access resources over the web, laying the groundwork for cloud computing services we use today.

Virtualization and Infrastructure-as-a-Service (2000s):
The next phase involved virtualization, which enabled multiple virtual machines to run on a single physical server. This innovation paved the way for Infrastructure-as-a-Service (IaaS) providers like Amazon Web Services (AWS), Microsoft Azure, and Google Cloud to offer scalable computing resources. These services allowed businesses to reduce hardware costs and improve operational efficiency.

The Rise of Hybrid Clouds (2010s-Present):
With the growing complexity of business environments, organizations began adopting hybrid cloud models, combining on-premises data centers with public cloud services. This offers a more flexible and cost-effective solution for handling different workloads, ensuring compliance, and achieving better disaster recovery.

Technical Summary:
Origins of Cloud Computing: Traces back to 1960s time-sharing systems and internet advancements in the 1990s.

Virtualization: Introduced the ability to run multiple virtual machines on a single server, which led to Infrastructure-as-a-Service (IaaS) providers.

Hybrid Cloud: Modern businesses now combine on-premises and cloud resources, balancing control, security, and scalability.

"""
propmt = "Summarize focusing on technical aspects: " + article_text

summary = summarizer(propmt, max_length=300, min_length=200, do_sample=False)
print("Summary: ", summary[0]['summary_text'])