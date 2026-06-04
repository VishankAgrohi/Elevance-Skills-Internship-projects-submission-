{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "810cc005-8add-439c-aefb-d2b6cd439122",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8c21b8c3-eb79-4e72-903e-df090f94e2bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/bin/python\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print(sys.executable)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "06d5c4fa-799f-48e7-b59e-97df569ca9e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: opencv-python in /opt/anaconda3/lib/python3.11/site-packages (4.10.0.84)\n",
      "Requirement already satisfied: numpy>=1.21.2 in /opt/anaconda3/lib/python3.11/site-packages (from opencv-python) (1.26.4)\n"
     ]
    }
   ],
   "source": [
    "!pip install opencv-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8a53dd65-1ec1-4231-ae96-03d4a67f35b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model Loaded Successfully\n"
     ]
    }
   ],
   "source": [
    "from tensorflow.keras.models import load_model\n",
    "\n",
    "model = load_model(\"car_color_model.keras\")\n",
    "print(\"Model Loaded Successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "73723d6b-2cfd-4d82-a734-6f704b73c269",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(None, 128, 128, 3)\n",
      "(None, 15)\n"
     ]
    }
   ],
   "source": [
    "from tensorflow.keras.models import load_model\n",
    "\n",
    "model = load_model(\"car_color_model.keras\")\n",
    "\n",
    "print(model.input_shape)\n",
    "print(model.output_shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5652993-fdfb-4c3f-a8e7-e802b16781a9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "182b9114-fc22-4972-b998-7af6ef1bdf1e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import filedialog, messagebox\n",
    "from PIL import Image, ImageTk\n",
    "import cv2\n",
    "import numpy as np\n",
    "from tensorflow.keras.models import load_model\n",
    "\n",
    "\n",
    "\n",
    "try:\n",
    "    model = load_model(\"car_color_model.keras\")\n",
    "except Exception as e:\n",
    "    messagebox.showerror(\"Model Error\", str(e))\n",
    "    raise\n",
    "\n",
    "\n",
    "class_names = ['beige',\n",
    "    'black',\n",
    "    'blue',\n",
    "    'brown',\n",
    "    'gold',\n",
    "    'green',\n",
    "    'grey',\n",
    "    'orange',\n",
    "    'pink',\n",
    "    'purple',\n",
    "    'red',\n",
    "    'silver',\n",
    "    'tan',\n",
    "    'white',\n",
    "    'yellow'\n",
    "]\n",
    "\n",
    "\n",
    "\n",
    "def predict_image():\n",
    "\n",
    "    file_path = filedialog.askopenfilename(\n",
    "        filetypes=[\n",
    "            (\"Image Files\", \"*.jpg *.jpeg *.png *.bmp\")\n",
    "        ]\n",
    "    )\n",
    "\n",
    "    if not file_path:\n",
    "        return\n",
    "\n",
    "    try:\n",
    "\n",
    "        # Display Original Image\n",
    "        pil_img = Image.open(file_path)\n",
    "\n",
    "        display_img = pil_img.copy()\n",
    "        display_img.thumbnail((500, 400))\n",
    "\n",
    "        photo = ImageTk.PhotoImage(display_img)\n",
    "\n",
    "        image_label.config(image=photo)\n",
    "        image_label.image = photo\n",
    "\n",
    "        # CNN Prediction\n",
    "        img = cv2.imread(file_path)\n",
    "\n",
    "        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
    "\n",
    "        img = cv2.resize(img, (128, 128))\n",
    "\n",
    "        img = img.astype(\"float32\") / 255.0\n",
    "\n",
    "        img = np.expand_dims(img, axis=0)\n",
    "\n",
    "        prediction = model.predict(img, verbose=0)\n",
    "\n",
    "        predicted_index = np.argmax(prediction)\n",
    "\n",
    "        predicted_color = class_names[predicted_index]\n",
    "\n",
    "        confidence = np.max(prediction) * 100\n",
    "\n",
    "        result_label.config(\n",
    "            text=f\"Predicted Colour: {predicted_color.upper()}\\nConfidence: {confidence:.2f}%\"\n",
    "        )\n",
    "\n",
    "    except Exception as e:\n",
    "\n",
    "        messagebox.showerror(\n",
    "            \"Prediction Error\",\n",
    "            str(e)\n",
    "        )\n",
    "\n",
    "\n",
    "\n",
    "root = tk.Tk()\n",
    "\n",
    "root.title(\"Car Colour Detection System\")\n",
    "\n",
    "root.geometry(\"800x700\")\n",
    "\n",
    "root.configure(bg=\"white\")\n",
    "\n",
    "heading = tk.Label(\n",
    "    root,\n",
    "    text=\"Car Colour Detection Using CNN\",\n",
    "    font=(\"Arial\", 20, \"bold\"),\n",
    "    bg=\"white\"\n",
    ")\n",
    "\n",
    "heading.pack(pady=20)\n",
    "\n",
    "upload_btn = tk.Button(\n",
    "    root,\n",
    "    text=\"Upload Car Image\",\n",
    "    command=predict_image,\n",
    "    font=(\"Arial\", 14),\n",
    "    width=20\n",
    ")\n",
    "\n",
    "upload_btn.pack(pady=10)\n",
    "\n",
    "image_label = tk.Label(\n",
    "    root,\n",
    "    bg=\"white\"\n",
    ")\n",
    "\n",
    "image_label.pack(pady=20)\n",
    "\n",
    "result_label = tk.Label(\n",
    "    root,\n",
    "    text=\"\",\n",
    "    font=(\"Arial\", 16, \"bold\"),\n",
    "    bg=\"white\",\n",
    "    fg=\"blue\"\n",
    ")\n",
    "\n",
    "result_label.pack(pady=20)\n",
    "\n",
    "footer = tk.Label(\n",
    "    root,\n",
    "    text=\"Internship Project - Car Colour Detection Model\",\n",
    "    font=(\"Arial\", 10),\n",
    "    bg=\"white\"\n",
    ")\n",
    "\n",
    "footer.pack(side=\"bottom\", pady=10)\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96c03ff6-463a-403f-9bf6-ae54ca42fc15",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2ad739b-4f4f-4388-83eb-6d35bab06a0e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eecfe6bc-7585-4c77-85de-e382aac19f59",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
