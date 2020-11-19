from cvxopt import matrix, spmatrix, solvers
import math
import numpy as np

# Set for cleaner output. Feel free to change this.
solvers.options['show_progress'] = False

class SVM(object):
    def __init__(self, points, labels):
        self.points = np.array(points)
        self.labels = np.array(labels)
        self.model = None

    def hard_margin(self):
        """
            For this problem, you need implement the constraints for
            the hard margin SVM classifier as a quadratic program. You can
            create a matrix or vector with:

            Q = matrix(...)

            This matrix data structure is specific to cvxopt. More
            documentation on how to create matrices is linked in the README.

            After you have set up the constraints, you should have
            something like

            self.model = solvers.qp(Q, l, G, h)
        """
        
        """ YOUR CODE HERE """
        self.P = matrix(2 * np.diag([1., 1., 0.]))
        self.q = matrix(np.array([0., 0., 0.])[:, None])
        y = np.arange(self.labels.shape[0], dtype=np.double)
        self.h = matrix(np.full_like(y, -1)[:, None])
        self.G = -self.labels[:, None] * self.points
        self.G = matrix(np.append(self.G,-self.labels[:, None], axis=1))

        self.model = solvers.qp(self.P, self.q, self.G, self.h, )

    def soft_margin(self, reg):
        """
            For this problem, you need to adapt the constraints you created
            for hard_margin to introduce slack variables (epsilon_i on the slides).
            You might find

            Q = spmatrix(...)

            helpful for this part, but feel free to construct the matrices however
            you like. Again, you need to end with

            self.model = solvers.qp(Q, l, G, h)
        """

        """ YOUR CODE HERE """

        P = spmatrix([2. * reg, 2. * reg], [0, 1], [0, 1], (3 + len(self.labels), 3 + len(self.labels)))
        q = matrix(np.append(np.zeros((3,1)), np.ones((len(self.labels), 1)))[:, None])
        y = np.arange(self.labels.shape[0], dtype=np.double)
        h = matrix(np.append(np.full_like(y, -1)[:, None], np.zeros(len(self.labels))))
        G = -self.labels[:, None] * self.points
        G = np.append(G,-self.labels[:, None], axis=1)
        G = matrix(np.append(G, np.diag([-1] * len(self.labels)), axis=1))
        extraConstraints = np.append(np.zeros((len(self.labels),3)), np.diag([-1] * len(self.labels)),axis=1)
        G = matrix(np.append(G, extraConstraints, axis=0))

        self.model = solvers.qp(P, q, G, h)


    def classify(self, point):
        """
            Return a label for the given point (+1, -1) based
            on the currently stored model which was set by
            either hard_margin or soft_margin.
        """

        if self.model is None:
            return 0

        """ YOUR CODE HERE """

        model = self.model['x']
        y = model[0] * point[0] + model[1] * point[1] + model[2]
        return np.sign(y)

    def get_hyperplane(self):
        """
            You are welcome to change the code here, but not required to.
            The autograder expects a list with [x_1, x_2, bias], which might
            be presented in a different order depending on how you set up
            your constraints.

            For the soft margin case, the model will include the slack variables.
            You may choose to return them or not.
        """

        if self.model is None:
            return None

        return self.model['x']
