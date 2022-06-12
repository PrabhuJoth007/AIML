class Perceptron:

    def activation(self):
        x = [1,4,5]

        w = [0.5,0.2,0.3]

        o = x[0]*w[0]+x[1]*w[1]+x[2]*w[2]

        sig = (1/(1+2.71828^(-o)))

        for i in range(0,5):

            target = 1

            n=0.1

            err = target-sig

            print(err)

            if(err==0):

                return sig

            if(err<0.05):

                return sig

            for j,k in x,w:

                k = k-n*err*j

y = Perceptron()

y.activation()
