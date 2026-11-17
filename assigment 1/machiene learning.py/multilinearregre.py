import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


class MultiplelinearRegression:

    def __init__(self, x1, x2, y):
        self.__x1 = np.array(x1)
        self.__x2 = np.array(x2)
        self.__y = np.array(y)

    def calculate(self):

        one = np.ones((len(self.__x1), 1), dtype=int)
        print(one)

        # Matrix
        self.x = np.c_[one, self.__x1, self.__x2]
        print("matrix:", self.x)

        # Transpose
        self.T = self.x.T
        print("Transpose:", self.T)

        # X transpose @ X
        self.multiply = self.T @ self.x
        print(self.multiply)

        # Inverse
        self.inv = np.linalg.pinv(self.multiply)
        print(np.round(self.inv, 2))

        # Inverse @ Transpose
        self.inv_m = self.inv @ self.T
        print(np.round(self.inv_m, 2))

        # Coefficients
        self.invm_y = self.inv_m @ self.__y
        print(self.invm_y)

        return self.invm_y

    def predict(self):

        a0 = self.invm_y[0]
        a1 = self.invm_y[1]
        a2 = self.invm_y[2]

        y_pred = a0 + (a1 * self.__x1) + (a2 * self.__x2)

        print(y_pred)

        return y_pred

    def draw_graphs(self):

        a0 = self.invm_y[0]
        a1 = self.invm_y[1]
        a2 = self.invm_y[2]

        # --------------------------------
        # GRAPH 1 : X1 vs Y
        # --------------------------------

        fig1 = plt.figure()

        plt.scatter(self.__x1, self.__y)

        plt.plot(
            self.__x1,
            a0 + (a1 * self.__x1) + (a2 * self.__x2)
        )

        plt.xlabel("X1")
        plt.ylabel("Y")
        plt.title("X1 vs Y")

        # --------------------------------
        # GRAPH 2 : X2 vs Y
        # --------------------------------

        fig2 = plt.figure()

        plt.scatter(self.__x2, self.__y)

        plt.plot(
            self.__x2,
            a0 + (a1 * self.__x1) + (a2 * self.__x2)
        )

        plt.xlabel("X2")
        plt.ylabel("Y")
        plt.title("X2 vs Y")

        # --------------------------------
        # GRAPH 3 : 3D REGRESSION PLANE
        # --------------------------------

        x1_grid, x2_grid = np.meshgrid(
            np.linspace(
                self.__x1.min(),
                self.__x1.max(),
                20
            ),

            np.linspace(
                self.__x2.min(),
                self.__x2.max(),
                20
            )
        )

        y_grid = (
            a0
            + (a1 * x1_grid)
            + (a2 * x2_grid)
        )

        fig3 = plt.figure()

        ax = fig3.add_subplot(
            111,
            projection='3d'
        )

        ax.scatter(
            self.__x1,
            self.__x2,
            self.__y
        )

        ax.plot_surface(
            x1_grid,
            x2_grid,
            y_grid,
            alpha=0.5
        )

        ax.set_xlabel("X1")
        ax.set_ylabel("X2")
        ax.set_zlabel("Y")

        ax.set_title(
            "Multiple Linear Regression"
        )

        return fig1, fig2, fig3

    def streamlit(self):

        st.title("Multiple Linear Regression")

        st.write(
            "Enter x1, x2 and y values"
        )

        x1_input = st.text_input(
            "Enter x1 values",
            "1,2,3,4,5"
        )

        x2_input = st.text_input(
            "Enter x2 values",
            "2,4,6,8,10"
        )

        y_input = st.text_input(
            "Enter y values",
            "10,20,30,40,50"
        )

        if st.button("Calculate"):

            try:

                x1 = [
                    float(i)
                    for i in x1_input.split(",")
                ]

                x2 = [
                    float(i)
                    for i in x2_input.split(",")
                ]

                y = [
                    float(i)
                    for i in y_input.split(",")
                ]

                # Length check
                if len(x1) != len(x2) or len(x1) != len(y):

                    st.error(
                        "x1, x2 and y values must have same length"
                    )

                else:

                    model = MultiplelinearRegression(
                        x1,
                        x2,
                        y
                    )

                    # Calculate
                    coefficients = model.calculate()

                    st.write("Coefficients:")
                    st.write(coefficients)

                    # Prediction
                    y_pred = model.predict()

                    st.write("Predicted values:")
                    st.write(y_pred)

                    # Graphs
                    fig1, fig2, fig3 = model.draw_graphs()

                    st.subheader("Graph 1: X1 vs Y")
                    st.pyplot(fig1)

                    st.subheader("Graph 2: X2 vs Y")
                    st.pyplot(fig2)

                    st.subheader(
                        "Graph 3: Regression Plane"
                    )
                    st.pyplot(fig3)

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )


# Run Streamlit
model = MultiplelinearRegression([], [], [])
model.streamlit()