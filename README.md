# TinyTiny Multimodal

a tiny vision language model

## project goals

Build a high-quality, low-hallucination vision language model small enough to
run on an edge device without a GPU.

## moondream0

Initial prototype built using SigLIP, Phi-1.5, and the LLaVa training dataset.
The model is for research purposes only, and is subject to the Phi and LLaVa
license restrictions.

 **Usage**
Clone this repository and install the dependencies:

```bash 
git clone https://github.com/vikhyat/moondream.git
cd moondream 
```

```bash
pip install -r requirements.txt
```

Use the `engine.py` script to run the model on CPU:

```bash
python engine.py --image [IMAGE_PATH] [--interactive]
```

When the `--interactive` flag is not set, the script will predict three questions and try
to answer them.

**Example**
| ![](assets/demo-1.jpg) |
```yaml
--2024-01-04 14:06:31--  https://raw.githubusercontent.com/vikhyat/moondream/main/assets/demo-1.jpg
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 284680 (278K) [image/jpeg]
Saving to: ‘demo-1.jpg’

demo-1.jpg          100%[===================>] 278.01K  --.-KB/s    in 0.003s  

2024-01-04 14:06:32 (81.8 MB/s) - ‘demo-1.jpg’ saved [284680/284680]

Fetching 12 files: 100% 12/12 [00:00<00:00, 26786.40it/s]

> what is this ?
The image features a person holding a book titled "The Little Book of Deep Learning" on a balcony. The balcony is located outside, with a view of a building in the background. The person appears to be enjoying the outdoor setting while reading the book.

> what does that book entail?
The book is titled "The Little Book of Deep Learning" and is written by French author Franco Florits. It is a comprehensive guide to deep learning, covering various aspects and techniques of machine learning and artificial intelligence. The book is designed to be accessible to both beginners and experienced professionals, providing practical insights and examples to help readers understand and apply deep learning concepts in their work.
```

**Limitations**

* The model may generate inaccurate statements.
* It may struggle to adhere to intricate or nuanced instructions.
* It is primarily designed to understand English. Informal English, slang, and
  non-English languages may not work well.
* The model may not be free from societal biases. Users should be aware of this
  and exercise caution and critical thinking when using the model.
* The model may generate offensive, inappropriate, or hurtful content if it is
  prompted to do so.
