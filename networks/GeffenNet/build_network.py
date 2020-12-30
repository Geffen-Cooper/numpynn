from NeuralNet import *
from make_data import *

def cluster_example():
    # build the network layer by layer
    net = Network(2, quadratic_cost_prime)
    net.add_fc_layer(4)
    net.add_sigmoid_layer(4)
    net.add_fc_layer(3)
    net.add_sigmoid_layer(3)

    # generate the data
    training_data, test_data, choices = gen_clusters()
    
    # train the network
    net.stochastic_gradient_descent(training_data,30,50,0.9,test_data)

    # test the network
    x_in = float(input("x:"))/500
    y_in = float(input("y:"))/500
    coord = np.array([[x_in,y_in]]).transpose()
    print(choices[np.argmax(net.forward_pass(coord))])
    x_in = float(input("x:"))/500
    y_in = float(input("y:"))/500
    coord = np.array([[x_in,y_in]]).transpose()
    print(choices[np.argmax(net.forward_pass(coord))])
    x_in = float(input("x:"))/500
    y_in = float(input("y:"))/500
    coord = np.array([[x_in,y_in]]).transpose()
    print(choices[np.argmax(net.forward_pass(coord))])

def train_mnist():
    training_data, testing_data = get_mnist()

    net = Network(784, quadratic_cost, quadratic_cost_prime)
    net.add_fc_layer(50)
    net.add_sigmoid_layer(50)
    net.add_fc_layer(10)
    net.add_sigmoid_layer(10)

    net.stochastic_gradient_descent(training_data,30,20,0.2,testing_data)

    file_store = open("net_50_hidden_30_epochs.pickle", "wb")
    pickle.dump(net, file_store)
    file_store.close()

if __name__ == "__main__":
# ======= Example 1, distinguish points in Clusters ============
    #cluster_example()

# ======= Example 2, classify handwritten digits ===============
    train_mnist() 
# ================= test the network ==========================
    # digit = Image.open("../../data/digit.png").convert('L')
    # digit = np.asarray(digit).astype(np.float32)/255
    # digit = digit.reshape(784,1)

    # file_store = open("net_15_epochs.pickle", "rb")
    # net = pickle.load(file_store)
    # file_store.close()

    # print("It is a ....", np.argmax(net.forward_pass(digit)))
    