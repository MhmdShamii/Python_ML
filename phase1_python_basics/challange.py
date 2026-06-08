import random

model_config ={
    "name"          : "MNIST_Model",
    "learning_rate" : 0.001,
    "epochs"        : 5,
    "batch_size"    : 32,
    "layers"        : [784, 128, 64, 10]
}
results = []

def gen_random(limOne, limTow):
    return random.uniform(limOne, limTow)

def simulate_epoch(epoch_num, prev_loss, prev_accuracy):
    return (
        prev_loss - gen_random(0.08, 0.15),    
        prev_accuracy + gen_random(0.08, 0.15) 
    )
def save_results(filename,result):
    with open(filename, "w") as f :
        for epoch in result:
            f.write(f"Epoch {epoch["Epoch"]}: loss= {epoch["loss"]}, accuracy= {epoch["accuracy"]} \n")

def summarize(results):
    best = max(results, key=lambda x: x["accuracy"])
    print(f"Training Complete!")
    print(f"Best accuracy : {best["accuracy"]}  (epoch {best["Epoch"]})")
    print(f"Final loss    : {results[-1]["loss"]}")
    print(f"Improvement   : +{round(best["accuracy"] -results[0]["accuracy"],2)} accuracy over 5 epochs")

def train(config):
    loss = 1.0
    accuracy = 0.3

    for epoch in range(config["epochs"]):
        loss , accuracy =  simulate_epoch(epoch,loss,accuracy)
        results.append( {
            "Epoch" :epoch+1,
            "loss" : round(loss,4),
            "accuracy" : round(accuracy,4)
        })
        print(f"{epoch+1}/{config["epochs"]}- loss= {results[epoch]["loss"]}, accuracy= {results[epoch]["accuracy"]}")
        
train(model_config)
save_results("phase1_python_basics/results.txt",results)
summarize(results)