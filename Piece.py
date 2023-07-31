class Piece:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rotations = []
        self.flipped = False
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.biggest = max(self.width, self.height)

    def produce_variants(self):
        work = self.matrix
        if work not in self.rotations:
            self.rotations.append(work)

        count = 0
        while count < 5 and True:
            temp = self.rotate(work)
            if temp in self.rotations:
                break

            self.rotations.append(temp)
            work = temp
            count += 1

        work = self.flip_x(self.matrix)
        if work not in self.rotations:
            self.flipped = True
            self.rotations.append(work)

            count = 0
            while count < 5 and True:
                temp = self.rotate(work)
                if temp in self.rotations:
                    break

                self.rotations.append(temp)
                work = temp
                count += 1

        work = self.flip_y(self.matrix)
        if work not in self.rotations:
            self.flipped = True
            self.rotations.append(work)

            count = 0
            while count < 5 and True:
                temp = self.rotate(work)
                if temp in self.rotations:
                    break

                self.rotations.append(temp)
                work = temp
                count += 1

    def flip_x(self, mat):
        out = []
        s = len(mat[0]) - 1
        for row in mat:
            out.append([row[s - x] for x, _ in enumerate(row)])
        return out

    def flip_y(self, mat):
        out = []
        s = len(mat) - 1
        for i in range(len(mat)):
            out.append([])
        for y, row in enumerate(mat):
            out[s - y] = list(row)
        return out

    def rotate(self, mat):
        width = len(mat[0])
        height = len(mat)
        out = []
        for _ in range(width):
            out.append([0 for _ in range(height)])

        try:
            for y, row in enumerate(mat):
                for x, value in enumerate(row):
                    out[x][height - 1 - y] = value
        except Exception as e:
            print(f"x={x}, y={y}, h={len(out)}, w={len(out[x])}")
            raise e
        return out

    def output(self, name=""):
        if name:
            print(f"Name={name}")
        print(f"Rotation count {len(self.rotations)}")
        # print(self.rotations)
        temp = []
        for i in range(self.biggest):
            temp.append(["." for _ in range((1 + self.biggest) * len(self.rotations))])

        for i, mat in enumerate(self.rotations):
            start = (1 + self.biggest) * i
            for y, row in enumerate(mat):
                for x, value in enumerate(row):
                    try:
                        if 1 == value:
                            temp[y][start + x] = "X"
                    except Exception as e:
                        print(f"x={x}, y={y}, start={start}, h={len(temp)}, w={len(temp[y])}")
                        raise e

        for text_matrix in temp:
            print("".join(text_matrix))
